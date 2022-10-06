import os
import tweepy

def handler(pd: "pipedream"):
    return_value = pd.steps["make_chart"]["$return_value"]
    dataset = return_value["dataset"]
    data = dataset["data"]
    alt_text = dataset["description"]
    text = dataset["title"]
    filename = return_value["filename"]

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
