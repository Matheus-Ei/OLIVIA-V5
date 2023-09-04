# Import the Libraries
import requests
import random


# Define the API URL and the autorization token
API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
headers = {"Authorization": "Bearer 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"}


# Define the system prompt
system = (
    "\nSistem: just below there is an inbox, "
    "in it everything that enters is summarized"
    "the summary maintains the meaning of the initial sentence, but with a much smaller size \n"
)

# Funcion to get the prompt
global i
i = 0
def get_prompt(input_user):
    global i
    if i == 0:
        i = i + 1
        prompt = system + "Input: " + input_user + "\n" + "Output:"
        return prompt
    
    else:
        prompt = "\nInput: " + input_user + "\n" + "Output:"
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

    responser = responser.split("Input:", -1)[-1]
    responser = responser.split("Output:", 1)[0]

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
        max_new_tokens=100,
        seed=random_seed,
        top_k = 500,
    )

    # Prompt input
    promp_input = {"inputs": intput, "parameters": generate_kwargs}

    # Request part
    response = requests.post(API_URL, headers=headers, json=promp_input)
    
    treated_response = delete_trash(response, history) # Delete the trash
    history = add_chatbot_return(treated_response, history) # Add the chatbot return to the history

    print("Output: " + treated_response) # Print the chatbot return
    return history, treated_response # Return the history and the chatbot return


# To test the code
if __name__ == "__main__":
    history = ""
    while True:
        chat = input("Input: ")
        history, resp = predict(input=chat, history=history)