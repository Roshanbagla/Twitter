""" To get information of the comanies from Wikipedia
"""
import json
import tweepy

CONSUMER_KEY = 'iScF8I4VohYJo29nJzXgf2V1S'
CONSUMER_SECRET = 'zfF41KtuCvceJpaIuhFCoHg5MwSncxcZpxx4o5X75xL5XsaQwi'

ACCESS_TOKEN = '4629343273-rJaTkC6mIHpW7tvgmD03jp0RS2Yl6Pa5PCTYG7e'              #access token
ACCESS_SECRET = 'FnYRFypEwdhBsB9ibyIaCWCcF5dxZu14fu2UwpruRZuGD'                  #acess_secret
AUTH = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
API = tweepy.API(AUTH)                  # creating an API object and
                                        #passing the authentication to it.

FINANCIAL_PARAMETERS = ['earnings', 'preview', 'rehash', 'executive turnover'
                        'dividends', 'board of director', 'new product', 'new customers'
                        'new investment', 'mergers', 'acquisitions', 'transaction', 'financial']
def get_tweet_text(status):
    """ function to return the text in a tweet.
    """
    return status._json['full_text']

def financial_check(tweet):
    """ function returning if it contains financial infomration or not.
    """
    if any(word in tweet for word in FINANCIAL_PARAMETERS):
        return tweet

def get_company_tweet():
    """ Code to extract the tweets of the companies
    """
    list_of_dictionary = []
    screen_name = '@'+ input('Enter the name of a company ')
    print(screen_name)
    for status in tweepy.Cursor(API.user_timeline,
                                screen_name=screen_name, tweet_mode='extended').items():
        tweet_dict = {}
        tweet_financial_check = financial_check(get_tweet_text(status))
        tweet_dict['tweet_text'] = tweet_financial_check
        if tweet_financial_check:
            list_of_dictionary.append(tweet_dict)
    return list_of_dictionary

DICT_OF_TWEETS = get_company_tweet()
for index in DICT_OF_TWEETS:
    print(json.dumps(index, indent=2))
