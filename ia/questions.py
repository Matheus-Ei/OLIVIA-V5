# Import the Libraries
import requests
import system.config.operations as op
import system.messages as msg

# Define the API URL and the autorization token
API_URL = op.load("system\config\ia.yaml", "bert_large")
headers = {"Authorization": "Bearer " + op.load("system\config\ia.yaml", "api_token")}

# Funcion to get the response
def response(question, context):
	prompt = {"inputs": {"question": question, "context": context}} # Define the prompt

	response = requests.post(API_URL, headers=headers, json=prompt) # Send the request to the API

    # Response tratament
	rr = response.json()
	try:
		response = rr[0]
		response = response["answer"]
		msg.error("Error to get the answer, triyng again with another config")
	except:
		try:
			response = rr["answer"]
			msg.error("Error to get the answer, triyng again with another config")
		except:
			response = rr

	return response # Return the response
	