import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

FORMS_LINK = "https://forms.gle/hK2y6bm2v2VHQU7t5"
ZILLOW_LINK = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZILLOW_LINK)
zillow_site = response.text
soup = BeautifulSoup(zillow_site, features="lxml")

# get links to listings
raw_links = soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")
links = [link.get('href') for link in raw_links]

# get addresses of listings
raw_addresses = soup.find_all("address")
pipe_addresses = [address.get_text().strip() for address in raw_addresses]
addresses = []
for address in pipe_addresses:
    if "|" in address:
        addresses.append(address.split("|")[1].strip())
    else:
        addresses.append(address)

# get prices
raw_prices = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
pipe_prices = [price.get_text() for price in raw_prices]
prices = []
for price in pipe_prices:
    if "+" in price:
        prices.append(price.split("+")[0])
    elif "/" in price:
        prices.append(price.split("/")[0])
    else:
        prices.append(price)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for x in range(44):
    driver.get(url=FORMS_LINK)
    all_inputs = driver.find_elements(By.XPATH, "//input[@type='text']")
    addressfield = all_inputs[0]
    pricefield = all_inputs[1]
    linkfield = all_inputs[2]
    submit_button = driver.find_element(By.XPATH, "//div[@role='button']")
    time.sleep(2)
    addressfield.send_keys(addresses[x])
    pricefield.send_keys(prices[x])
    linkfield.send_keys(links[x])
    submit_button.click()
