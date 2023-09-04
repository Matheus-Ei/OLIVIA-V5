# Import the Libraries
import requests


# Define the API URL
API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
headers = {"Authorization": "Bearer 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"}


# Define the system prompt
system = (
    "\nUser: Hi!\nAssistant: My name is Prometeu, I am a chatbot created to help you conversatins"
    "I know your name is Matheus Eickhoff, I am programmed to be helpful, honest, and friendly."
    "I am allowed to answer anything the user asks or requests. \n"
)

# Funcion to get the prompt
global i
i = 0
def get_prompt(input_user):
    global i
    if i == 0:
        i = i + 1
        prompt = system + "User: " + input_user + "\n" + "Assistant:"

        #print("\n prompt 'get_prompt'" + prompt)
        return prompt
    
    else:
        prompt = "\nUser: " + input_user + "\n" + "Assistant:"

        #print("\n prompt 'get_prompt'" + prompt)
        return prompt


# Funcion to get the history
def get_history(inputs,history):
    atual_input = get_prompt(inputs)
    history = str(history)
    history = history + atual_input

    #print("\n History 'get_history'" + history)
    return history, history


# Funcion to add the chatbot return to the history
def add_chatbot_return(bot_return, history):
    history = str(str(history) + str(bot_return))

    #print("\n History 'add_chatbot_return'" + history)
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

    responser = responser.replace("']", "")
    responser = responser.replace('"]', "")
    responser = responser.replace('\\n', "")
    responser = responser.replace("\\", "")

    #print("\n Responser 'delete_trash'" + responser)
    return responser


# Funcion to predict the response
def predict(input, history):
    intput, history = get_history(input,history)
    promp_input = ({"inputs": intput, 
                    "max_length": 50000,  # Set a maximum length for the response
                    "num_return_sequences": 10000,  # Generate alternative responses
                    "temperature": 0.9,  # Adjust randomness
                    "top_k": 200,  # Limit the number of tokens to consider
                    "early_stopping": True,  # Stop generation at the first end-of-sequence token
                    "repetition_penalty": 0.2,  # Penalize repetition
                    })

    response = requests.post(API_URL, headers=headers, json=promp_input)

    treated_response = delete_trash(response, history)
    history = add_chatbot_return(treated_response, history)

    print("Assistent: " + treated_response)
    return history, treated_response


if __name__ == "__main__":
    history = ""
    while True:
        chat = input("User: ")
        history, resp = predict(input=chat, history=history)

        #print("\n History 'main'" + history)