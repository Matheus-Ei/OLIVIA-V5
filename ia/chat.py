# Import the Libraries
import requests
import random
import re
import system.messages as msg


# Define the API URL and the autorization token
#API_URL = "https://api-inference.huggingface.co/models/timdettmers/guanaco-33b-merged"
API_URL = "https://api-inference.huggingface.co/models/Phind/Phind-CodeLlama-34B-v2"
#API_URL = "https://api-inference.huggingface.co/models/WizardLM/WizardCoder-Python-34B-V1.0"
headers = {"Authorization": "Bearer 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"}

intentions = "{GENERATE_IMAGE}, {SPEAK_TIME}, {SEARCH_ON_GOOGLE}, {PAUSE_MUSIC}, {PLAY_MUSIC}, {NEXT_MUSIC}, {SPEAK_WEATHER}"

# Define the system prompt
system = (
    "\nSistem: Lívia is an artificial intelligence created to talk with the user"
    "Lívia is tuned to be helpful, honest, friendly, and emotional"
    "and is allowed to answer anything the user asks or requests \n"
    "Possible Intentions=" + intentions + "\n"
    "User: can you help me? \n"
    "Assistant: Sure,, what do you need help? \n"
    "User: can you generate an image for me?\n"
    "Assistant: Yes i can, here is it: {GENERATE_IMAGE} \n"
    "User: can you pause the music to me?\n"
    "Assistant: Ok i will pause the music {PAUSE_MUSIC} \n"
    "User: tell me the time \n"
    "Assistant: Of course, here is the current time: {SPEAK_TIME}\n"
    "User: tell me the weather forecast for tomorrow \n"
    "Assistant: Sure, here's the weather forecast: {SPEAK_WEATHER} \n"
    "User: thanks for the help. \n"
    "Assistant: No problem, whenever you need it, just call \n"
)

# Funcion to get the prompt
global i
i = 0
def get_prompt(input_user):
    global i
    if i == 0:
        i = i + 1
        prompt = system + "User: " + input_user + "\n" + "Assistant:"
        return prompt
    
    else:
        prompt = "\nUser: " + input_user + "\n" + "Assistant:"
        return prompt


# Funcion to get the history
def get_history(inputs,history):
    atual_input = get_prompt(inputs)
    history = str(history)
    history = history + atual_input
    return history, history


# Funcion to add the chatbot return to the history
def add_chatbot_return(bot_return, history):
    history = str(str(history) + str(bot_return))
    return str(history)


# Funcion to delete the trash
def delete_trash(response, history):
    response = response.json()
    history = str(history)

    # Select the content inside the generated_text
    response = [item['generated_text'] for item in response][0]
    responser = str(response) # Convert to string

    # Split the responses between the user and the chatbot
    exitt = []
    responser = responser.split("User:")
    for resp in responser:
        respt = resp.split("Assistant:")
        for it in respt:
            exitt.append(it)

    # Split the history between the user and the chatbot
    exitt_hist = []
    resp_history = history.split("User:")
    for resp_h in resp_history:
        respt_h = resp_h.split("Assistant:")
        for it_h in respt_h:
            exitt_hist.append(it_h)


    # Delete the intersection
    for itm in exitt_hist:
        if itm in exitt:
            exitt.remove(itm)

    responser = list(exitt)[0] # Get the chatbot return

    # Delete the trash
    responser = responser.replace("']", "")
    responser = responser.replace('"]', "")
    responser = responser.replace('\n', "")

    #print("Responser: " + responser)
    #print("History: " + history)

    return responser # Return the chatbot return


# Funcion to get the intention if have one
def get_intent(response):
    if "{intent=" in response:
        responser = response.split("{intent=")[0]

        intent = response.split("{intent=")[1]
        intent = intent.replace("}", "")
        intent = intent.lower()

        msg.informative("Intent: " + intent)
        return responser, intent
    
    else:
        return response, "None"


# Funcion to predict the response
def predict(input, history):
    msg.informative("Chatbot Funcion")
    intput, history = get_history(input,history)
    random_seed = random.randint(0, 50)

    # Dict with the parameters
    generate_kwargs = dict(
        max_new_tokens=50,
        seed=1,
        top_k = 500,
    )

    # Prompt input
    promp_input = {"inputs": intput, "parameters": generate_kwargs}

    # Request part
    #print(promp_input)
    response = requests.post(API_URL, headers=headers, json=promp_input)
    
    treated_response = delete_trash(response, history) # Delete the trash
    history = add_chatbot_return(treated_response, history) # Add the chatbot return to the history

    treated_response, intent = get_intent(treated_response) # Get the intention if have one

    return history, treated_response, intent # Return the history and the chatbot return


# To test the code
if __name__ == "__main__":
    history = ""
    while True:
        chat = input("User: ")
        history, resp, intent = predict(input=chat, history=history)
        #print(history)
        #print("Assistent: " + resp)
        #print("Intent: " + intent + "\n")
