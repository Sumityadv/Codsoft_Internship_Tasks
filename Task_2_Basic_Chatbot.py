import re                                                                                      # importing regular expression module for pattern matching

def load_responses(Task_2_Basic_Responses):
    responses = {}
    with open(Task_2_Basic_Responses, 'r') as file:
        for line in file:                                                                       # this function will read lines from txt file and store it in dictionary      
            pattern, response = line.strip().split(': ')                                       
            responses[pattern] = response
    return responses

Task_2_Basic_Responses = load_responses('Task_2_Basic_Responses.txt')

def Bot_basic_response(user_input):
    user_input = user_input.lower()
    
    for pattern, basic_response in Task_2_Basic_Responses.items():                                    #this function will check for pattern matching and resposes by user and also covert in lower case the user input
        if re.search(pattern, user_input): 
            return basic_response

    return "Sorry I am unable to answer it now, in future i will be able to answer it"

print("Hello! I'm a basic Bot. You can start by Greetings.")
while True:
    user_input = input("You: ")                                                                #this function will be the real time where the resposes will be given by bot and the user will be able to interact with bot
    if user_input.lower() == 'exit':
        print("Bot: tata bye!")
        break
    basic_response = Bot_basic_response(user_input)
    print("Bot:", basic_response)
