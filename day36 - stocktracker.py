import os
from datetime import datetime, timedelta
import html
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Retrieve stock data; determine degree of shift between two days ago and yesterday
AV_API = os.environ.get("AV_API_TOKEN")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
yday = (datetime.now() - timedelta(days=1)).strftime(("%Y-%m-%d"))
twodays = (datetime.now() - timedelta(days=2)).strftime(("%Y-%m-%d"))
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_API
}
stock_data = requests.get(STOCK_ENDPOINT, params=stock_parameters).json()
yday_close = float(stock_data["Time Series (Daily)"][yday]["4. close"])
twodays_close = float(stock_data["Time Series (Daily)"][twodays]["4. close"])
delta = round(100 - (yday_close / twodays_close * 100))
if delta < 0:
    string_change = f"🔻{str(delta * -1)}%"
else:
    string_change = f"🔺{str(delta)}%"

# Retrieve top 3 stories with headlines and briefs as a function
NEWSAPI = os.environ.get("NEWSAPI_TOKEN")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_parameters = {
    "q": html.escape(COMPANY_NAME),
    "apiKey": NEWSAPI,
    "language": "en"
}
def get_news():
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters).json()
    top_3 = news_response["articles"][slice(3)]
    headlines = [x["title"] for x in top_3]
    briefs = [x["description"] for x in top_3]
    return headlines, briefs

# if delta is greater than 5% then send delta and top story
account_sid = os.environ.get("TWILIO_ID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)
from_number = os.environ.get("TWILIO_NUMBER")
to_number = os.environ.get("CELL_NUMBER")
if -5 < delta < 5:
    pass
else:
    news = get_news()
    message = client.messages.create(from_=from_number,
    body=f"{STOCK}: {string_change} \n Headline: {news[0][0]} \n Brief: {news[1][0]}",
    to=to_number
    )

print(message.sid)
