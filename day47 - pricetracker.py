import os
import requests
from bs4 import BeautifulSoup
import smtplib

EMAIL = os.environ.get("EMAIL_ADDRESS")
APP_PASS = os.environ.get("GOOGLE_APP_PASS")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept-Language": "en-US,en;q=0.5"
}

url = "https://www.amazon.com/Sauce-Sichuan-Chili-Crisp-Ounce/dp/B0849Q133Y"

response = requests.get(url, headers=headers)
result = response.text

soup = BeautifulSoup(result, features="lxml")

title = soup.find(id="productTitle").get_text().strip()
price_span = soup.find("span", class_="a-offscreen")
price = price_span.next_element
price_float = float(price.split("$")[1])

TARGET_PRICE = 10

if price_float < TARGET_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=APP_PASS)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price alert!\n\n{message}\n{url}".encode("utf-8")
            )