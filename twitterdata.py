""" Code to extract the tweets and date stamp of a company
"""

import tweepy

CONSUMER_KEY = 'iScF8I4VohYJo29nJzXgf2V1S'
CONSUMER_SECRET = 'zfF41KtuCvceJpaIuhFCoHg5MwSncxcZpxx4o5X75xL5XsaQwi'

ACCESS_TOKEN = '4629343273-rJaTkC6mIHpW7tvgmD03jp0RS2Yl6Pa5PCTYG7e'              #access token
ACCESS_SECRET = 'FnYRFypEwdhBsB9ibyIaCWCcF5dxZu14fu2UwpruRZuGD'                  #acess_secret
AUTH = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
API = tweepy.API(AUTH)                  # creating an API object and
                                        #passing the authentication to it.

screen_name = '@'+ input('Enter the name of a company ')
def get_tweet_text(status):
    """ function to return the text in a tweet.
    """
    return status._json['full_text']

def get_tweet_time(status):
    """ function to return the time a tweet was created
    """
    return status._json['created_at']

def get_company_tweet():
    """ Code to extract the tweets of the companies
    """
    list_of_dictionary = []
    print(screen_name)
    for status in tweepy.Cursor(API.user_timeline,
                                screen_name=screen_name, tweet_mode='extended').items():
        tweet_dict = {}
        tweet_dict['tweet_text'] = get_tweet_text(status)
        #tweet_dict['time_stamp'] = get_tweet_time(status)
        #tweet_dict['company_name'] = screen_name
        list_of_dictionary.append(tweet_dict)
    return list_of_dictionary

DICT_OF_TWEETS = get_company_tweet()
FILE = open('tweet.txt', 'a')
FILE.write("***********************" + screen_name + "***********************")
FILE.write("\n")
FILE.write("        ")
for index in range(0, len(DICT_OF_TWEETS)):
    FILE.write((DICT_OF_TWEETS[index]['tweet_text']))
    FILE.write("\n")
FILE.close()
