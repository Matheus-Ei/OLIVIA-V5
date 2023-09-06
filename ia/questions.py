# Import the Libraries
import requests

# Define the API URL and the headers
API_URL = "https://api-inference.huggingface.co/models/deepset/bert-large-uncased-whole-word-masking-squad2"
headers = {"Authorization": "Bearer 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"}

# Funcion to get the response
def response(question, context):
	prompt = {"inputs": {"question": question, "context": context}} # Define the prompt

	response = requests.post(API_URL, headers=headers, json=prompt) # Send the request to the API

	# Response tratament
	response = response.json()
	response = response["answer"]

	return response # Return the response
	