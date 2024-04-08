import requests
from datetime import datetime
import smtplib

MY_LAT = ********* # Your latitude
MY_LONG = ********* # Your longitude
email_addr = "***************"
password = "*************"

def iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and \
            MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now.hour > sunset or time_now.hour < sunrise:
        return True

if iss_close() and dark():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email_addr, password=password)
        connection.sendmail(from_addr=email_addr, to_addrs=email_addr, msg=f"Subject: ISS Overhead!\n \nLook up!")
