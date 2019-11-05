from twitterscraper import query_tweets
import pandas as pd
import sys
sys.stdin = open('동이름.txt', 'r')
dong_list = []
for _ in range(467):

    dong_list.append(input())



if __name__ == '__main__':

    for dong in dong_list:
        modDfObj = pd.DataFrame(columns=['user_id', 'tweet_id', "likes", "text", "loc"])
        list_of_tweets = query_tweets(dong, 100)
        for tweet in list_of_tweets:
            temp = {}
            temp["user_id"] = tweet.user_id
            temp["tweet_id"] = tweet.tweet_id
            temp["likes"] = tweet.likes
            temp["text"] = tweet.text
            temp["loc"] = dong
            modDfObj = modDfObj.append(temp, ignore_index=True)

        modDfObj.to_csv(f'./data_dong/{dong}.txt', mode="w")
