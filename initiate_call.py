import africastalking
import os
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get('AT_USERNAME')
api_key = os.environ.get('AT_APIKEY')
at_number = os.environ.get('AT_NUMBER')

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