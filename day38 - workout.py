import os
import datetime as dt
import requests

APP_ID = os.environ.get("NUT_APP_ID")
API_KEY = os.environ.get("NUT_APP_KEY")
WEIGHT_KG = 124.7
HEIGHT_CM = 182.9
AGE = 40
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/d795c01e4e83ffe6a1a63f1080d2f9a5/myWorkouts/workouts"
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
whatdo = input("What exercise did you do?")

params = {
    "query": whatdo,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(NUTRI_ENDPOINT, headers=headers, json=params)
result = response.json()

day = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%H:%M:%S")
exercise = result["exercises"][0]["name"].title()
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]

new_line = {
    "workout": {
        "date": day,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}
sheety_headers = {"Authorization": SHEETY_TOKEN}
sheety_response = requests.post(SHEETY_ENDPOINT, json=new_line, headers=sheety_headers)
sheety_result = sheety_response.json()
print(sheety_result)
