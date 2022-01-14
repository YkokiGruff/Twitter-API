import tweepy
import requests
import config_main
import json

API_Key = config_main.API_KEY
API_Sec = config_main.API_SECRET_KEY
Token = config_main.ACCESS_TOKEN
Token_Sec = config_main.ACCESS_TOKEN_SECRET
Bearer_Token = config_main.BEARER_TOKEN

auth = tweepy.OAuthHandler(API_Key, API_Sec)
auth.set_access_token(Token, Token_Sec)
api = tweepy.API(auth)

tweets = api.home_timeline(count=5)


for tweet in tweets:
    print('='*20)
    print('ツイートID : '   , tweet.id)
    print('ツイート時間 : ' , tweet.created_at)
    print('ツイート本文 : ', tweet.text)
    print('ユーザ名 : ', tweet.user.name) 
    print('スクリーンネーム : ', tweet.user.screen_name) 
    print('フォロー数 : ', tweet.user.friends_count) 
    print('フォロワー数 : ', tweet.user.followers_count) 
    print('ユーザ概要 : ', tweet.user.description) 
    print('='*20)

def connect_to_twitter(key):
    return {"Authorization": "Bearer {}".format(key)}

#検索実行
def make_request(headers):
    url = "https://api.twitter.com/2/tweets/search/recent"
    params = "query=from:learningnao"
    return requests.request("GET", url, params=params, headers=headers).json()




headers = connect_to_twitter(Bearer_Token)
response = make_request(headers)
print(response)