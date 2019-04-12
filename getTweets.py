import tweepy
import re
from tweepy import OAuthHandler
from textblob import TextBlob



class TwitterClient(object):

    def __init__(self):
        ''' 
        Class constructor or initialization method. 
        '''
        # keys and tokens from the Twitter Dev Console 
        consumer_key = 'tNe7VzrlP8oshJooEegzKBVdA'
        consumer_secret = 'GBNwRDr3akwKNbSDj0uinHVHaSdyVThpuf0wIoMRWxM58UNYzW'
        access_token = '1115703385737445376-ailYxJOl4cXTtbUy9DNnhiPZX6kXTm'
        access_token_secret = 'RIf5XuF4IlHpxeNbcWSKAXVdJh3yq0FTdwYzYGQG1x1ke'

        # attempt authentication 
        try: 
            # create OAuthHandler object 
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
            # set access token and secret 
            self.auth.set_access_token(access_token, access_token_secret) 
            # create tweepy API object to fetch tweets 
            self.api = tweepy.API(self.auth) 
        except: 
            print("Error: Authentication Failed") 
            
    def clean_tweet(self, tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        cleaned = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split()) 
        return cleaned

    def get_tweets(self, query, count = 10):
        tweets = []

        try: 
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count) 

            for tweet in fetched_tweets:

                parsed_tweet = {}

                parsed_tweet['text'] = tweet.text 
                parsed_tweet["sentiment"] = "0"

        
        except tweepy.TweepError as e:
            print("Error: " + str(e))



def main():
    twitterAPI = TwitterClient()

    tweets = twitterAPI.get_tweets("",10)

    




if __name__ == "__main__":
    main()