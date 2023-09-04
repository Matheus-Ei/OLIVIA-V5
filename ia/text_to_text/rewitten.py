# Import libraries
import requests

# Define the API URL and the autorization token
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
headers = {"Authorization": "Bearer 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"}

# Define the funcion prompt
def rewite(inputt):
    inputt = 'rewrite the sentence in other words: " ' + str(inputt) + ' "' # Define the input

    # Dict with the parameters
    generate_kwargs = dict(
        temperature=1,
        max_new_tokens=100,
        top_k = 50,
    )

    promp_input = {"inputs": inputt, "parameters": generate_kwargs} # Prompt input
    
    response = requests.post(API_URL, headers=headers, json=promp_input) # Request part

    print(response.json())
    return response.json() # Return the response