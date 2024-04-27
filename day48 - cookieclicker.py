import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chromedriver = webdriver.ChromeOptions()
chromedriver.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromedriver)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
store = driver.find_element(By.ID, "store")

bot_timeout = time.time() + 300

def get_prices():
    upgrades = store.find_elements(By.TAG_NAME, "div")
    prices = [upgrade for upgrade in upgrades if
               upgrade.text != "" and upgrade.get_attribute("class") != "grayed"]
    return prices

def buy_item():
    price_list = get_prices()
    price_list[-1].click()

botrunning = True
while botrunning:
    timeout = time.time() + 5
    while time.time() < timeout:
        cookie.click()
    buy_item()
    if time.time() > bot_timeout:
        botrunning = False
