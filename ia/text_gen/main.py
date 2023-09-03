# Import the Libraries
import requests
from text_generation import Client, InferenceAPIClient


# Define the API URL
API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
headers = {"Authorization": "Bearer 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"}


# Pre Define Variables
global i
i = 0
global chatbot
chatbot = []


system = (
    "\nUser:  Hi!\nAssistant:  My name is Prometeu, I am a chatbot created to help you with everything"
    "I know your name is Matheus Petri Eickhoff, and your biggest dream is to become a billionaire like Iron Man "
    "I am not human, but you programmed me to be able to interpret scenes and emotions that you describe to me"
    "but I am programmed to be helpful, polite, honest, and friendly.\n"
)


def get_prompt(input_user):
    global i
    print("-->Getting prompt<--")
    if i == 0:
        i = 1 + 1
        prompt = system + "User: " + input_user + "\n" + "Assistant: "
        return prompt
    
    else:
        prompt = "User: " + input_user + "\n" + "Assistant: "
        return prompt


def get_history(inputs,history):
    print("-->Getting history<--")

    atual_input = get_prompt(inputs)
    history = str(history) + str(atual_input)
    return history


def add_chatbot_return(bot_return, history):
    history = str(history) + str(bot_return) + "\n"
    return history


def delete_trash(response, history):
    print("-->Deleting trash<--")
    response = response.json()
    history = str(history)

    # Selecionar o conteúdo dentro de 'generated_text'
    response = [item['generated_text'] for item in response]
    response = str(response)


    # Dividir a string com base em "Assistant" e manter a parte após "Assistant"
    response.replace(history, "")

    responser = response.split("Assistant:", -1)[-1]
    responser = responser.split("User:", 1)[0]
    responser = responser.replace("']", "")
    responser = responser.replace('"]', "")
    responser = responser.replace('\\n', "")

    print(responser)
    return response, responser



def predict(input, history):
    promp_input = get_history(input,history)
    promp_input = ({"inputs": promp_input})

    response = requests.post(API_URL, headers=headers, json=promp_input)

    history, treated_response = delete_trash(response, history)
    add_chatbot_return(treated_response, history)

    return history, treated_response


if __name__ == "__main__":
        while True:
            history = ""
            input_user = input("User: ")
            history, treated_response = predict(input_user, history)
