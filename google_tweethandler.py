""" To search a query and retrive the links
"""
from googlesearch import search


def extract_twitter_handle(name_company):
    """ function will return the first 2 links of a company from a query searched
        on google.com
    """
    query_on_google = name_company +" twitter"
    print("    ")
    print(query_on_google)
    for result in search(query_on_google, tld="com.au", num=1, stop=1, pause=2):
        result = result[20:]
        position = result.find('?')
        company_tweet_name = result[:position]
        print("The twitter name of the company is "+ company_tweet_name)
        TWEET_HANDLE.write(company_tweet_name)


FILE = open('companies_name.txt', 'r')
COMPANY = FILE.read()
COMPANY = COMPANY.split('|')
TWEET_HANDLE = open('tweet_handle.txt', 'w')
for word in list(COMPANY):
    extract_twitter_handle(word)
TWEET_HANDLE.close()
