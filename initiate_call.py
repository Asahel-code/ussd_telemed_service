import africastalking
import os
from dotenv import load_dotenv

load_dotenv()

username = 'musat'
api_key = 'eb98c94d1854bd11d797e702f4eaff766ca62d751add2e68c0f50a6d423722cf'
at_number = '+254702639254'

africastalking.initialize(username, api_key)

voice = africastalking.Voice

class VOICE:
    def __init__(self, call_to):
        self.call_to = call_to

    def call(self):

        try:
			# Make the call
            result =voice.call(callFrom = at_number, callTo = [self.call_to])
            print (result)
        except Exception as e:
            print ("Encountered an error while making the call:%s" %str(e))

call_to = "+254742079321"
make_call = VOICE(call_to)
make_call.call()