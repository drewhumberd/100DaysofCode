import random
import smtplib
import datetime as dt
import pandas as pd

email_addr = "***************"
password = "*************"
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    with open("supportfiles/quotes.txt") as quotef:
        quotes = quotef.readlines()
    message = f"Subject: Hello!\n \n{random.choice(quotes)}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email_addr, password=password)
        connection.sendmail(from_addr=email_addr, to_addrs=email_addr, msg=message)

birthdays = pd.read_csv("supportfiles/birthdays.csv")
birth = birthdays.to_dict(orient="records")

for entry in birth:
    if entry["month"] == now.month and entry["day"] == now.day:
        with open(f"supportfiles/letter_templates/letter_{random.randrange(1, 3)}.txt") as letter:
            text = letter.read()
            finish = text.replace("[NAME]", entry["name"])
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=email_addr, password=password)
                connection.sendmail(from_addr=email_addr, to_addrs=email_addr, msg=f"Subject: Happy Birthday!\n \n{finish}")
