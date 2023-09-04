# Import the Libraries
import requests

# Load the model and tokenizer
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}


# Funcion to sumarize the text
def sumarize(text):
    print("--> Starting the sumarize funcion <--")
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
        temperature=1.0,
        max_length=300,
        min_length=100,)

    try:
        # Prompt input
        promp_input = {"inputs": text, "parameters": generate_kwargs}

        response = requests.post(API_URL, headers=headers, json=promp_input)

        print("--> Ending the sumarize funcion <--")

        ret = response.json()
        ret = ret[0]
        ret = ret["summary_text"]  # Correct the key to lowercase

        return str(ret)  # Return the response
    except:
        print("#####==->Sumarizer Error<-==#####")