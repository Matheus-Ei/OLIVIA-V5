# Import the Libraries
import requests
import random
import system.config.operations as op


# Define the API URL and the autorization token
API_URL = op.load("system\config\ia.yaml", "wizard_coder")
headers = {"Authorization": "Bearer " + op.load("system\config\ia.yaml", "api_token")}


# Funcion to delete the trash
def delete_trash(response, history):
    response = response.json()
    history = str(history)

    # Select the content inside the generated_text
    response = [item['generated_text'] for item in response][0]
    responser = response # Convert to string


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
        respt_h = resp_h.split("Assistent:")
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
    system = (
        "Sistem: the Assistent separates the main message contained within the User\n"
        "User: send to sister hello can you go with bella to the park\n"
        "Assistent: hello can you go with bella to the park\n"
        f"User: {input}\n"
        "Assistent:"
    )

    # Dict with the parameters
    generate_kwargs = dict(
        max_new_tokens=50,
    )

    # Prompt input
    promp_input = {"inputs": str(system), "parameters": generate_kwargs}
    response = requests.post(API_URL, headers=headers, json=promp_input)

    responser = delete_trash(response, system) # Delete the trash
    return responser # Return the chatbot return


# To test the code
if __name__ == "__main__":
    while True:
        chat = input("User: ")
        resp = predict(input=chat)
        print("Assistent: " + resp)
