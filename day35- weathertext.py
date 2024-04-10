import requests
from twilio.rest import Client
import os
account_sid = os.environ.get("TWILIO_ID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
my_lat= 42.76252871047145
my_lon= -71.50888146173483

parameters = {
    "lat": my_lat,
    "lon": my_lon,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(weather_endpoint, params=parameters)
response.raise_for_status()
data = response.json()
forecast = data["list"]
weather_list = [x["weather"][0]["id"] for x in forecast]
for x in weather_list:
    if x < 700:
        message = client.messages.create(from_=from_number,
        body='Bring an umbrella.',
        to=to_number
        )

        print(message.sid)