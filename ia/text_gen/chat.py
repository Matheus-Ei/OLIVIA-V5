# Import the Libraries
import requests
import random


# Define the API URL and the autorization token
#API_URL = "https://api-inference.huggingface.co/models/timdettmers/guanaco-33b-merged"
API_URL = "https://api-inference.huggingface.co/models/Phind/Phind-CodeLlama-34B-v2"
headers = {"Authorization": "Bearer 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"}


# Define the system prompt
system = (
    "\nSistem: Prometeu is an artificial intelligence created to talk with the user"
    "Prometheus is tuned to be helpful, honest, friendly, and emotional"
    "and is allowed to answer anything the user asks or requests. \n"
    "User: hello how are u? \n"
    "Assistant: I'm fine, thank you. How are you? \n"
    "User: i am fine to, lets chat? \n"
    "Assistant: Sure, what do you want to talk about? \n"
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
    response = [item['generated_text'] for item in response]
    responser = str(response)

    responser = responser.split("Assistant:", -1)[-1]
    responser = responser.split("User", 1)[0]
    responser = responser.split("#", 1)[0]

    responser = responser.replace("']", "")
    responser = responser.replace('"]', "")
    responser = responser.replace('\\n', "")
    responser = responser.replace("\\", "")

    return responser


# Funcion to predict the response
def predict(input, history):
    intput, history = get_history(input,history)
    random_seed = random.randint(0, 50)

    # Dict with the parameters
    generate_kwargs = dict(
        temperature=0.3,
        max_new_tokens=50,
        seed=random_seed,
        top_k = 1000,
    )

    # Prompt input
    promp_input = {"inputs": intput, "parameters": generate_kwargs}

    # Request part
    response = requests.post(API_URL, headers=headers, json=promp_input)
    
    treated_response = delete_trash(response, history) # Delete the trash
    history = add_chatbot_return(treated_response, history) # Add the chatbot return to the history

    print("Assistent: " + treated_response) # Print the chatbot return
    return history, treated_response # Return the history and the chatbot return


# To test the code
if __name__ == "__main__":
    history = ""
    while True:
        chat = input("User: ")
        history, resp = predict(input=chat, history=history)
