import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

def tweet(text):  
    client = tweepy.Client(consumer_key=os.environ.get("TWITTER_API_KEY"),
                           consumer_secret=os.environ.get("TWITTER_API_SECRET"),
                           access_token=os.environ.get("TWITTER_ACCESS_TOKEN"),
                           access_token_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"))

    tweet = client.create_tweet(text=text)
    return tweet
    
def upload_image(filename, alt_text, text):
    auth = tweepy.OAuth1UserHandler(
        os.environ.get("TWITTER_API_KEY"),
        os.environ.get("TWITTER_API_SECRET"),
        os.environ.get("TWITTER_ACCESS_TOKEN"),
        os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
    )
    api = tweepy.API(auth)

    response = api.media_upload(filename=filename)
    api.create_media_metadata(response.media_id_string, alt_text=alt_text)
    tweet = api.update_status(media_ids=[response.media_id_string], status=text)
    return tweet