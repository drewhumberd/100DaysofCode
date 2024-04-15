import os
import smtplib
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)
from_number = os.environ.get("TWILIO_NUMBER")
to_number = os.environ.get("CELL_NUMBER")

class NotificationManager:
    '''Class responsible for sending messages via Twilio API.'''
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self, message):
        send_text = self.client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print(send_text.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )