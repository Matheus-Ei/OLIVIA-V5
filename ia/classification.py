# Import the Libraries
import requests
import random
import system.config.operations as op


# Define the API URL and the autorization token
API_URL = op.load("system\config\ia.yaml", "phind_code_llama")
headers = {"Authorization": "Bearer " + op.load("system\config\ia.yaml", "api_token")}

# Define the tasks
tasks = "{GENERATE_IMAGE}, {ASKING_SCHEDULE}, {SEARCH_ON_GOOGLE},{NONE}"

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
        "\nSistem: when the input enters, the model classifies it into which type of task from the following options:\n"
        f"Possibles Tasks: {tasks}"
        "User: hello how are u?"
        "Assistent: NONE"
        "User: hey, can you generate a image to me please?"
        "Assistent: {GENERATE_IMAGE}"
        "User: livia, talk the weather please"
        "Assistent: {TALK_WEATHER}"
        f"User: {input}"
        "Assistent:"
    )

    random_seed = random.randint(0, 50)

    # Dict with the parameters
    generate_kwargs = dict(
        #max_new_tokens=10,
        seed=random_seed,
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
