import requests
# newsapi website

quary=input("what news are u intrested today?:")
api_key=input("enter API KEY:") # 7380129f93a840c2b272006b0839a4f6

url=f"https://newsapi.org/v2/everything?q={quary}a&from=2026-02-09&sortBy=publishedAt&apiKey={api_key}"

print(url)

r=requests.get(url)

data=r.json()
news_article=data["articles"]

for index, article in enumerate(news_article):
    print(index+1,article["title"],"\n", article["url"])
    print("\n-------------------------------------------------------\n")