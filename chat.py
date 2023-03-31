import random

# define a list of possible responses
responses = [
    "Hello!",
    "How are you?",
    "What can I help you with?",
    "Sorry, I didn't understand that.",
    "Goodbye!"
]

# define a function to generate a response
def generate_response(input):
    return random.choice(responses)

# main loop
while True:
    # get input from user
    input = input("You: ")
    
    # generate response
    response = generate_response(input)
    
    # print response
    print("Bot: " + response)
    
    # exit loop if user says goodbye
    if response == "Goodbye!":
        break
