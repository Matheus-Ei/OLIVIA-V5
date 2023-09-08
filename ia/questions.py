# Import the Libraries
import requests
import system.config.operations as op

# Define the API URL and the autorization token
API_URL = op.load("system\config\ia.yaml", "bert_large")
headers = {"Authorization": "Bearer " + op.load("system\config\ia.yaml", "api_token")}

# Funcion to get the response
def response(question, context):
	prompt = {"inputs": {"question": question, "context": context}} # Define the prompt

	response = requests.post(API_URL, headers=headers, json=prompt) # Send the request to the API

	# Response tratament
	response = response.json()
	#response = response[0]
	response = response["answer"]

	return response # Return the response
	