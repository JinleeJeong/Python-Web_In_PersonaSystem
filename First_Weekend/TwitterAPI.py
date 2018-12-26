import tweepy

consumer_key = "l5vhsjm9T0GqbSuvl5rNm3jFn"
consumer_secret = "SHr2qwTQCy9ILnGKoT0xDZGYWBjxLnSvNy4asid9xabfX3O3dm"
access_token = "1074942618201554944-ZwHIO6ulTJW7sitA09u1j21diyfKvZ"
access_token_secret = "1dwFFjJ8abn5mWxWCCks0Hdbv3mFlRDhqsOQgUyuycUJT"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)  


# location = "%s,%s,%s" % ("35.95", "128.25", "1000km") # 검색기준(대한민국 중심) 좌표, 반지름

keyword = "okey"  # OR 로 검색어 묶어줌, 검색어 5개(반드시 OR 대문자로)

result = []
for i in range(1, 3):
    tweets = api.search(keyword)
    for tweet in tweets:
        result.append([tweet.text])

for a in range(1, 10):
    print(''.join(result[a]))
