# Import the Libraries
import requests
import random
import re
#import system.messages as msg


#API_URL = "https://api-inference.huggingface.co/models/timdettmers/guanaco-33b-merged"
#API_URL = "https://api-inference.huggingface.co/models/WizardLM/WizardCoder-Python-34B-V1.0"

# Define the API URL and the autorization token
API_URL = "https://api-inference.huggingface.co/models/Phind/Phind-CodeLlama-34B-v2"
headers = {"Authorization": "Bearer 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"}
file = r"ia\last_conversations.txt"

def get_system(file):
    # Funcion to Get the last lines of the file
    def get_last_lines(file):
        array = []
        # Open the file
        with open(file, "r") as f:
            tamanho = len(f.readlines())
            print(tamanho)

            # Read the lines
            linhas = file.readlines()

            # If the file have more than 4 lines
            array = list(linhas)

                
            
            # Retorna as últimas 4 linhas do arquivo.
            us1 =  array[tamanho]
            us1 = str(us1) + "\n"
            ass1 = array[tamanho-1]
            ass1 = str(ass1) + "\n"
            us2 = array[tamanho-2]
            us2 = str(us2) + "\n"
            ass2 = array[tamanho-3]
            ass2 = str(ass2) + "\n"

            return us1, ass1, us2, ass2


    commands = "{GENERATE_IMAGE}, {TALK_CURRENT_TIME}, {SEARCH_ON_GOOGLE}, {WEATHER_FORECAST}"
    us1, ass1, us2, ass2 = get_last_lines(file)


    system = (
        "\nSistem: Lívia is an artificial intelligence created to talk with the user"
        "Lívia is tuned to be helpful, honest, friendly, and emotional"
        "and is allowed to answer anything the user asks or requests,"
        "if the user requests Lívia can use commands to perform tasks for the user\n"
        "Commands: " + commands + "\n"
        "User: can you help me? \n"
        "Assistant: Sure, what do you need help? \n"
        f"{us1}"
        f"{ass1}"
        f"{us2}"
        f"{ass2}"
    )

    return system

system = get_system(file)


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


def write_line_file(file, text):
# Abre o arquivo para escrita.
  with open(file, "a") as f:
    # Escreve a linha no arquivo.
    f.write("\n" + text)


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
        responser = response.split("command:")[0]

        intent = response.split("command:")[1]
        intent = intent.lower()

        #msg.informative("Command: " + intent)
        return responser, intent
    
    else:
        return response, "None"


# Funcion to predict the response
def predict(input, history):
    #msg.informative("Chatbot Funcion")
    write_line_file(file, input)

    intput, history = get_history(input,history)
    random_seed = random.randint(0, 50)

    # Dict with the parameters
    generate_kwargs = dict(
        max_new_tokens=50,
        seed=random_seed,
        top_k = 5000,
    )

    # Prompt input
    promp_input = {"inputs": intput, "parameters": generate_kwargs}

    # Request part
    #print(promp_input)
    response = requests.post(API_URL, headers=headers, json=promp_input)
    
    treated_response = delete_trash(response, history) # Delete the trash
    history = add_chatbot_return(treated_response, history) # Add the chatbot return to the history

    treated_response, intent = get_intent(treated_response) # Get the intention if have one
    write_line_file(file, treated_response)

    return history, treated_response, intent # Return the history and the chatbot return


# To test the code
if __name__ == "__main__":
    history = ""
    while True:
        chat = input("User: ")
        history, resp, intent = predict(input=chat, history=history)
        print("History " + history)
        print("Assistent: " + resp)
        print("Intent: " + intent + "\n")
