# Import the Libraries
import requests
import system.messages as msg

# Define the API URL and the headers
API_URL = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"
headers = {"Authorization": "Bearer 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"}

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