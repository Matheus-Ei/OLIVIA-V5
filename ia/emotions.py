# Import the Libraries
import requests
import system.messages as msg
import system.config.operations as op

# Define the API URL and the autorization token
API_URL = op.load("system\config\ia.yaml", "roberta_emotion")
headers = {"Authorization": "Bearer " + op.load("system\config\ia.yaml", "api_token")}

# Funcion to say the emotions
def predict(inputs):
	# Define the prompt
	prompt = {"inputs": inputs} 

	response = requests.post(API_URL, headers=headers, json=prompt) # Send the request to the API

	# Response tratament
	response = response.json()
	response = response[0]
	response = response[0]
	response = response["label"]
	msg.informative("Emotion: " + str(response)) # Print the emotion

	return response # Return the response