import os
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
