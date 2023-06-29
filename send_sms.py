import africastalking
import os
from dotenv import load_dotenv

load_dotenv()

username = 'musat'
api_key = 'eb98c94d1854bd11d797e702f4eaff766ca62d751add2e68c0f50a6d423722cf'


africastalking.initialize(username, api_key)

sms = africastalking.SMS

class SMSClient:
    def __init__(self, phone_number, message):
        self.phone_number = phone_number
        self.message = message

    def send_sms(self):
        sms.send(self.message, [self.phone_number], callback=on_finish)
        

def on_finish(error, response):
    if error is not None:
        raise error
    print(response)