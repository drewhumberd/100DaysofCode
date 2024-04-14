import os
import requests
import datetime as dt
from day39.flight_data import FlightData

KIWI_TOKEN = os.environ.get("KIWI_TOKEN")
KIWI_HEADERS = {"apikey": KIWI_TOKEN}
KIWI_SERVER = "https://api.tequila.kiwi.com"
KIWI_LOCATIONS = "/locations/query"
KIWI_SEARCH = "/v2/search"
HOME_CITY = "LON"
class FlightSearch:
    '''Class responsible for retrieving flight data from the Kiwi API.'''
    def get_city_code(self, city):
        params = {
            "term": city
        }
        response = requests.get(f"{KIWI_SERVER}{KIWI_LOCATIONS}", \
                                headers=KIWI_HEADERS, params=params)
        result = response.json()
        city_code = result["locations"][0]["code"]
        code = city_code
        return code

    def get_prices(self, city_code):
        now = dt.datetime.now().strftime("%d/%m/%Y")
        sixmo = (dt.datetime.now() + dt.timedelta(days=180)).strftime(("%Y-%m-%d"))
        params = {
            "fly_from": HOME_CITY,
            "fly_to": city_code,
            "date_from": now,
            "date_to": sixmo,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
            "one_for_city": 1,
            "max_stopovers": 0
        }
        response = requests.get(f"{KIWI_SERVER}{KIWI_SEARCH}", \
                                headers=KIWI_HEADERS, params=params)
        result = response.json()
        try:
            data = result["data"][0]
        except IndexError:
            print(f"No flights found for {city_code}.")
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        return flight_data
