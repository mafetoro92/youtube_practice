import tweepy
import typing


def upload_tweet(list_for_merge: typing.List[str]) -> None:
    consumer_key = '84uNzaL0HFDs3cCTEIqA94fLc'
    consumer_secrect = 'Gxm9uBoGtpZrAQon8IyY31rT9DQ2QijmHDMHyaAXvDP6q2BrYk'

    Access_token = '1269054827385978886-RZ5BOociazCU68f8kfRrF8xPEqb0AF'
    Access_token_secret = 'm1CeTqn5UYFzZOHm8gqGX071NWGCqaPVufGLpJolCMiu0'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secrect)
    auth.set_access_token(Access_token, Access_token_secret)
    api = tweepy.API(auth)

    for info in list_for_merge:
        tweet_text = 'I am download ' + info + ' video using python'
        api.update_status(tweet_text)
