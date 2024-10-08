#  Social Media Dashboard (basic)
import requests

def fetch_tweets(hashtag):
    url = f"https://api.twitter.com/2/tweets/search/recent?query={hashtag}"
    headers = {"Authorization": "Bearer YOUR_BEARER_TOKEN"}
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    hashtag = input("Enter a hashtag to search: ")
    tweets = fetch_tweets(hashtag)
    print(tweets)
