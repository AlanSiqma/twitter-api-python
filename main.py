import tweepy
import auth_twitter

auth = auth_twitter.auth_handler()
api = tweepy.API(auth)


def send_tweet(message):
    api.update_status(message)


send_tweet("Happy Coding!" + " #LearnPython")
