""" Code to extract the user_name
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

def get_user_name():
    """ Code to get the user_name of a company
    """
    screen_name = input('Enter the name of a company ')
    user = API.get_user(screen_name=screen_name)
    print(user.name)

get_user_name()
