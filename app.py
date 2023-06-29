from flask import Flask, request
import os
from send_sms import SMSClient
from initiate_call import VOICE

app = Flask(__name__)

@app.route('/ussd', methods=['POST', 'GET'])

def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    sms_phone_number = ["+254742079321"]
    sms_phone_number.append(phone_number)

    call_back_client(phone_number)
    #ussd logic
    if text == "":
        #main menu
        response = "Welcome to TelAfya. Choose your service:\n"
        response += "1. Connect to telemedicine service\n"
        response += "2. Reach out to a hospital\n"
        response += "3. Reach out for an ambulance\n"
        response += "4. Exit"

    #sub menu 
    elif text == "1":
        response = "Please describe your symptoms:\n"

        try:
            #sending the sms
            message = text

            sms_client = SMSClient(sms_phone_number, message)
            sms_client.send_sms()

            response = "Message has been send to you phone number about your enquiry, welcome back again."
        except Exception as e:
            #show us what went wrong
            print(f"We have a problem: {e}")

    elif text == "2":
        response = "Please select the hospital you would like to reach out to:\n"
        response += "1. Kenyatta Hospital\n"
        response += "2. Mama lucy Hospital\n"
        response += "3. Mbagathi Hospital\n"
        response += "4. Mater Hospital"
    
    elif text == "3":
        call_to = "+254742079321"
        make_call = VOICE(call_to)
        make_call.call()

        response = "Call has been initiated be patient as we connect you to an ambulance service."

    elif text == "4":
       response = "Thank you for using our services, welocome back again."
    
    #sub sub menu
    elif text == "2*1":
        call_to = "+254742079321"
        make_call = VOICE(call_to)
        make_call.call()

        response = "Call has been initiated be patient as we connect you to Kenyatta Hospital."

    elif text == "2*2":
        call_to = "+254742079321"
        make_call = VOICE(call_to)
        make_call.call()

        response = "Call has been initiated be patient as we connect you to Mama lucy Hospital."

    elif text == "2*3":
        call_to = "+254742079321"
        make_call = VOICE(call_to)
        make_call.call()

        response = "Call has been initiated be patient as we connect you to Mbagathi Hospital."

    elif text == "2*4":
        call_to = "+254742079321"
        make_call = VOICE(call_to)
        make_call.call()

        response = "Call has been initiated be patient as we connect you to  Mater Hospital."

    else:
        response = "Invalid input. Try again."

    return response

@app.route('/call', methods=['POST'])

def call_back_client():
    return '<Response> <Dial phoneNumbers=%phone_number% maxDuration="5"/></Response>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))