import africastalking
import os
from dotenv import load_dotenv

load_dotenv()

username = 'sandbox' 
api_key = 'b703cc98d2d552496bc8da745bf92a73288def5a51e28de1c248741cda1dbd62'
at_number = '+254713544692'

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
