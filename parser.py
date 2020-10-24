from dateutil import parser
import tweepy
from tweepy import API
try:
    import json
except ImportError:
    import simplejson as json
import re
import sys
import time
import pymorphy2
from nltk.corpus import stopwords
stop = set(stopwords.words("english")) | set(stopwords.words("russian"))
morph = pymorphy2.MorphAnalyzer()
from pprint import pprint

start_time = time.time()


def get_twitter_auth():
    try:
        access_token = ''
        access_secret = ''
        consumer_key = ''
        consumer_secret = ''
    except KeyError:
        sys.stderr.write("No Environment args")
        sys.exit(1)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth


def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth_handler=auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return client


if __name__ == '__main__':
    user = "@MELANIATRUMP"
    client = get_twitter_client()
    i = 0
    # f_txt = open('text.txt', 'w', encoding='utf-8')
    for tweet in tweepy.Cursor(client.user_timeline, screen_name=user).items():
        i += 1
        print(i)
        jsn = tweet._json
        # pprint(jsn)
        text = jsn['text']
        if 'extended_tweet' in jsn:
            text = jsn['extended_tweet']['full_text']
        if 'retweeted_status' in jsn:
            text = jsn['retweeted_status']['text']
        date = jsn['created_at']
        date = parser.parse(date)
        text = str(text)
        print(date)
        print(text)
        # f_txt.write(str(jsn))
        # f_txt.write('\n')