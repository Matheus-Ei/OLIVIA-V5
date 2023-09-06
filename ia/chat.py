# Import the Libraries
import requests
import random
import re
#import system.messages as msg


# Define the API URL and the autorization token
#API_URL = "https://api-inference.huggingface.co/models/timdettmers/guanaco-33b-merged"
API_URL = "https://api-inference.huggingface.co/models/Phind/Phind-CodeLlama-34B-v2"
headers = {"Authorization": "Bearer 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"}

intentions = "GENERATE_IMAGE, SPEAK_TIME"

# Define the system prompt
system = (
    "\nSistem: Lívia is an artificial intelligence created to talk with the user"
    "Lívia is tuned to be helpful, honest, friendly, and emotional"
    "and is allowed to answer anything the user asks or requests. \n"
    "Possible Intentions: " + intentions + "\n"
    "User: hello how are u? \n"
    "Assistant: I'm fine, thank you. How are you? \n"
    "User: i am fine to, can you help me? \n"
    "Assistant: Sure, what do you need help? \n"
    "User: can you generate an image for me? \n"
    "Assistant: Yes i can, here is it: {intent=GENERATE_IMAGE} \n"
    "User: what time is it? \n"
    "Assistant: Now it is: {intent=TELL_HOUR} \n"
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

    # Selecionar o conteúdo dentro de 'generated_text'
    response = [item['generated_text'] for item in response][0]
    responser = str(response)
    
    #responser = responser.split("Assistant:", -1)[-1]
    #responser = responser.split("User", 1)[0]
    exitt = []
    responser = responser.split("User:")
    for resp in responser:
        respt = resp.split("Assistant:")
        for it in respt:
            exitt.append(it)


    exitt_hist = []
    resp_history = history.split("User:")
    for resp_h in resp_history:
        respt_h = resp_h.split("Assistant:")
        for it_h in respt_h:
            exitt_hist.append(it_h)


    exitt_hist = set(exitt_hist)
    exitt = set(exitt)

    intersect = exitt.intersection(exitt_hist)
    # Deleta os itens da interseção de array1
    for inter in intersect:
        exitt.remove(inter)

    responser = list(exitt)[0]
    #print(list(exitt))

    responser = responser.replace("']", "")
    responser = responser.replace('"]', "")

    return responser


# Funcion to get the intention if have one
def get_intent(response):
    if "{intent=" in response:
        responser = response.split("{intent=")[0]

        intent = response.split("{intent=")[1]
        intent = intent.replace("}", "")

    
        return responser, intent
    
    else:
        return response, "none"


# Funcion to predict the response
def predict(input, history):
    #msg.informative("Starting the Chatbot Funcion")
    intput, history = get_history(input,history)
    random_seed = random.randint(0, 50)

    # Dict with the parameters
    generate_kwargs = dict(
        temperature=0.3,
        max_new_tokens=200,
        seed=random_seed,
        top_k = 10000,
    )

    # Prompt input
    promp_input = {"inputs": intput, "parameters": generate_kwargs}

    # Request part
    response = requests.post(API_URL, headers=headers, json=promp_input)
    
    treated_response = delete_trash(response, history) # Delete the trash
    history = add_chatbot_return(treated_response, history) # Add the chatbot return to the history

    treated_response, intent = get_intent(treated_response)

    #msg.informative("Ending the Chatbot Funcion")
    return history, treated_response, intent # Return the history and the chatbot return


# To test the code
if __name__ == "__main__":
    history = ""
    while True:
        chat = input("User: ")
        history, resp, intent = predict(input=chat, history=history)
        print("Assistent: " + resp)
        print("Intent: " + intent + "\n")
        #print("\n"+history)
