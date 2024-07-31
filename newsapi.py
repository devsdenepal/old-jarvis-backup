import requests
URL=('https://newsapi.org/v2/top-headlines?')
def get_articles():
    response = requests.get(URL,params='country=us&apiKey=20e4798bd250402382c18e07ee7abe04')
    articles = response.json()['articles']
    results = []
    for article in articles:
        results.append({"title": article["title"]})
    for result in results:
        print(result["title"])
print(get_articles())