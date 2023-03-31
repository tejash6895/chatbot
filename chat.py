import openai_secret_manager
import openai
import random

# load OpenAI API key
secrets = openai_secret_manager.get_secret("openai")
openai.api_key = secrets["api_key"]

# define a list of possible responses
responses = [
    "Hello!",
    "How are you?",
    "What can I help you with?",
    "Sorry, I didn't understand that.",
    "Goodbye!"
]

# define a function to generate a response using ChatGPT
def generate_response(input):
    response = openai.Completion.create(
      engine="davinci",
      prompt=(f"User: {input}\nBot: "),
      temperature=0.5,
      max_tokens=50,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response.choices[0].text.strip()

# main loop
while True:
    # get input from user
    input = input("You: ")
    
    # generate response using ChatGPT
    response = generate_response(input)
    
    # if the response is empty, use a random response from the list
    if not response:
        response = random.choice(responses)
    
    # print response
    print("Bot: " + response)
    
    # exit loop if user says goodbye
    if response == "Goodbye!":
        break
