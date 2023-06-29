import africastalking
import os
from dotenv import load_dotenv

load_dotenv()

username = 'sandbox'
api_key = '9148ad44ff6a499cce2c59edb353fbf5756418209e0b7ba9baa142e3c1aafae4'
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

call_to = "+254742079321"
make_call = VOICE(call_to)
make_call.call()