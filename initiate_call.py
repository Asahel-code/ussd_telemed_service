import africastalking
import os
from dotenv import load_dotenv

load_dotenv()

username = 'musat' 
api_key = 'd46fe22e676feddca9f9dffec26e9c0d380858ea8846eee19e505bd0091974a6'
at_number = '+254730731050'

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
