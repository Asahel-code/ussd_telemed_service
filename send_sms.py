import africastalking
import os
from dotenv import load_dotenv

load_dotenv()


username = 'sandbox' 
api_key = 'b703cc98d2d552496bc8da745bf92a73288def5a51e28de1c248741cda1dbd62'


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

# message = 'wassup'
# sms_client = SMSClient('+254702639254', message)
# sms_client.send_sms()