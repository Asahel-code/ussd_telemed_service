import openai
import os
from dotenv import load_dotenv

openai.api_key = os.environ.get('OPEN_API_KEY')  

def med_ai(message):
    prompt = "User: " + message + "\nChatGPT:"

    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the GPT-3 model
        prompt=prompt,
        max_tokens=50,  # Adjust the response length as desired
        n = 1,  # Set the number of responses to generate
        stop=None,  # Customize the stopping condition for responses
        temperature=0.7  # Adjust the temperature for response randomness
    )

    chatbot_response = response.choices[0].text.strip().split('\n')[0].replace("ChatGPT:", "")

    return chatbot_response

# mess =med_ai('headache')
# print(mess)