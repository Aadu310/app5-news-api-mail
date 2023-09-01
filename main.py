import requests
from send_email import send_email

topic = "elektrobit"
api_key = "9333164fc3754bc0b74906091e4de29b"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-08-01&" \
      "sortBy=publishedAt&" \
      "apiKey=9333164fc3754bc0b74906091e4de29b&language=en"
# make a request
request = requests.get(url)

# get a dictionary with data
context = request.json()


# access the article titles and description
body = ""
for article in context["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
               + "\n" + body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
