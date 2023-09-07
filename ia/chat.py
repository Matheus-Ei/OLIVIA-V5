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
            linhas = f.readlines()
            tamanho = len(linhas)

            # If the file have more than 4 lines
            array = list(linhas)
            

            # Retorna as últimas 4 linhas do arquivo.
            us1 =  array[tamanho-4]
            us1 = str(us1)

            ass1 = array[tamanho-3]
            ass1 = str(ass1)

            us2 = array[tamanho-2]
            us2 = str(us2)

            ass2 = array[tamanho-1]
            ass2 = str(ass2)


            return us1, ass1, us2, ass2


    us1, ass1, us2, ass2 = get_last_lines(file)


    system = (
        "\nSistem: Lívia is an artificial intelligence created to talk with the user"
        "Lívia is tuned to be helpful, honest, friendly, and emotional"
        "and is allowed to answer anything the user asks or requests.\n"
        f"{us1}"
        f"{ass1}"
        f"{us2}"
        f"{ass2}"
        " \nAssistent:"
    )
    return system


system = get_system(file)


# Funcion to get the prompt
global i
def get_prompt(input_user):
    prompt = "\nUser: " + input_user + "\n" + "Assistent:"
    return prompt


def write_line_file(file, text, type):
    if type == "assis":
        # Abre o arquivo para escrita.
        with open(file, "a") as f:
            # Escreve a linha no arquivo.
            f.write("\nAssistent: " + text)
    elif type == "user":
        # Abre o arquivo para escrita.
        with open(file, "a") as f:
            # Escreve a linha no arquivo.
            f.write("\nUser: " + text)


# Funcion to delete the trash
def delete_trash(response, history):
    response = response.json()
    history = str(history)

    # Select the content inside the generated_text
    response = [item['generated_text'] for item in response][0]
    responser = response # Convert to string
    #print(responser)


    # Split the responses between the user and the chatbot
    exitt = []
    responser = responser.split("User:")
    for resp in responser:
        respt = resp.split("Assistent:")
        for it in respt:
            exitt.append(it)

    # Split the history between the user and the chatbot
    exitt_hist = []
    resp_history = history.split("User:") 
    for resp_h in resp_history:
        respt_h = resp_h.split("Assistent:") or history.split("\nAssistent:")
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

    return responser # Return the chatbot return


# Funcion to predict the response
def predict(input):
    write_line_file(file, input, "user")
    system = get_system(file)
    #msg.informative("Chatbot Funcion")

    random_seed = random.randint(0, 50)

    # Dict with the parameters
    generate_kwargs = dict(
        max_new_tokens=100,
        seed=random_seed,
        #top_k = 5000,
    )

    # Prompt input
    promp_input = {"inputs": str(system), "parameters": generate_kwargs}

    # Request part
    #print(system)
    response = requests.post(API_URL, headers=headers, json=promp_input)
    
    treated_response = delete_trash(response, system) # Delete the trash

    write_line_file(file, treated_response, "assis")
    
    system = get_system(file)

    return treated_response # Return the history and the chatbot return


# To test the code
if __name__ == "__main__":
    while True:
        chat = input("User: ")
        resp = predict(input=chat)
        print("Assistent: " + resp)
