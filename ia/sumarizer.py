# Import the Libraries
import requests
import system.messages as msg
import system.config.operations as op

# Define the API URL and the autorization token
API_URL = op.load("system\config\ia.yaml", "facebook_bart_large")
headers = {"Authorization": "Bearer " + op.load("system\config\ia.yaml", "api_token")}


# Funcion to sumarize the text
def sumarize(text):
    msg.informative("Starting the sumarize funcion")
    text = text.replace("\n", "") # Remove the \n
    text = text.replace("\t", "") # Remove the \t
    text = text.replace("\r", "") # Remove the \r
    text = text.replace('"', "") # Remove the "
    text = text.replace("'", "") # Remove the '
    text = text.replace("”", "") # Remove the ”
    text = text.replace("“", "") # Remove the “
    text = text.replace("(", "") # Remove the (
    text = text.replace(")", "") # Remove the )
    text = text.replace("[", "") # Remove the [
    text = text.replace("]", "") # Remove the ]
    text = text.replace("{", "") # Remove the {
    text = text.replace("}", "") # Remove the }
    text = text.replace(":", "") # Remove the :
    text = text.replace(";", "") # Remove the ;
    text.lower() # Convert to lower case
    

    # Dict with the parameters
    generate_kwargs = dict(
        max_length=300,
        min_length=100,)

    try:
        # Prompt input
        promp_input = {"inputs": text, "parameters": generate_kwargs}

        response = requests.post(API_URL, headers=headers, json=promp_input)

        msg.informative("Ending the Sumarize Funcion")

        ret = response.json()
        ret = ret[0]
        ret = ret["summary_text"]  # Correct the key to lowercase

        return str(ret)  # Return the response
    except:
        msg.error("Sumarizer Error")