import os
import requests

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_ENDPOINT = "https://api.sheety.co/d795c01e4e83ffe6a1a63f1080d2f9a5/flightDeals/prices"
sheety_headers = {"Authorization": SHEETY_TOKEN}

class DataManager:
    '''Class responsible for working with Google Sheet via Sheety API.'''
    def __init__(self):
        self.dest_data = {}

    def get_dest_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        data = response.json()
        self.dest_data = data["prices"]
        return self.dest_data

    def update_sheet(self):
        for x in self.dest_data:
            json = {"price": {"iataCode": x["iataCode"]}}
            sheety_response = requests.put(f"{SHEETY_ENDPOINT}/{x['id']}", json=json,\
                                           headers=sheety_headers)
            sheety_response.raise_for_status()
