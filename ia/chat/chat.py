# Import the Libraries
import requests
import random
import system.messages as msg
import system.config.operations as op



# Define the API URL and the autorization token
API_URL = op.load("system\config\ia.yaml", "phind_code_llama")
headers = {"Authorization": "Bearer " + op.load("system\config\ia.yaml", "api_token")}

# Define the file to save the last conversations
file = r"ia\chat\last_conversations.txt"

# Funcion to Get the system variable
def get_system(file):
    # Funcion to Get the last lines of the file
    def get_last_lines(file):
        array = []
        # Open the file
        with open(file, "r") as f:
            linhas = f.readlines()
            tamanho = len(linhas) # Get the number of lines

            # If the file have more than 4 lines
            array = list(linhas) # Convert to list
            
            # Recover the last lines
            us1 =  array[tamanho-4]
            us1 = str(us1)
            ass1 = array[tamanho-3]
            ass1 = str(ass1)
            us2 = array[tamanho-2]
            us2 = str(us2)
            ass2 = array[tamanho-1]
            ass2 = str(ass2)

            return us1, ass1, us2, ass2 # Return the last lines

    us1, ass1, us2, ass2 = get_last_lines(file) # Get the last lines

    # Define the system variable
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
    return system # Return the system variable
system = get_system(file) # Get the system variable


# Funcion to get the prompt
def get_prompt(input_user):
    prompt = "\nUser: " + input_user + "\n" + "Assistent:"
    return prompt


# Funcion to write the line in the file
def write_line_file(file, text, type):
    if type == "assis":
        # Open the file to write
        with open(file, "a") as f:
            # Write the line in the file
            f.write("\nAssistent: " + text)
    elif type == "user":
        # Open the file to write
        with open(file, "a") as f:
            # Write the line in the file
            f.write("\nUser: " + text)


# Funcion to delete the trash
def delete_trash(response, history):
    response = response.json() # Convert json
    history = str(history) # Convert to string

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
    write_line_file(file, input, "user") # Write the user input in the file
    system = get_system(file) # Update the system variable
    msg.informative("Chatbot Funcion")

    random_seed = random.randint(0, 50) # Define the random seed

    # Dict with the parameters
    generate_kwargs = dict(
        max_new_tokens=100,
        seed=random_seed,
        #top_k = 5000,
    )

    # Prompt input
    promp_input = {"inputs": str(system), "parameters": generate_kwargs}

    # Request part
    response = requests.post(API_URL, headers=headers, json=promp_input)
    
    treated_response = delete_trash(response, system) # Delete the trash

    write_line_file(file, treated_response, "assis") # Write the chatbot return in the file
    system = get_system(file) # Update the system variable

    return treated_response # Return the chatbot return


# To test the code
if __name__ == "__main__":
    while True:
        chat = input("User: ")
        resp = predict(input=chat)
        print("Assistent: " + resp)
