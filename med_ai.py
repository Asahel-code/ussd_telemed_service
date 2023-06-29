import openai

openai.api_key = "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"

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

# message=med_ai('hi how are you')
# print(message)
