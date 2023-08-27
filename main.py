import requests

api_key = "9333164fc3754bc0b74906091e4de29b"
url = "https://newsapi.org/v2/everything?q=elektrobit&" \
      "from=2023-07-27&sortBy=publishedAt&" \
      "apiKey=9333164fc3754bc0b74906091e4de29b"
# make a request
request = requests.get(url)

# get a dictionary with data
context = request.json()

# access the article titles and description
for article in context["articles"]:
      print(article["title"])
      print(article["description"])
