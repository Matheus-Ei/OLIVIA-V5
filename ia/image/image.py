# Import the Libraries
import io
from PIL import Image
import requests


# Define the API URL and the headers
TEXT_API_URL = "https://api-inference.huggingface.co/models/daspartho/prompt-extend"
API_URL = "https://api-inference.huggingface.co/models/DucHaiten/DucHaitenJourney"
headers = {"Authorization": "Bearer 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"}


# Define the prompt function
def prompt(input_prompt):
	# Prompt tratament
	input_prompt = "Generated Prompt " + input_prompt
	generate_kwargs = dict(
        max_new_tokens=100,
    )
	
	output = ({"inputs": input_prompt, "parameters": generate_kwargs}) # Define the output
	response = requests.post(TEXT_API_URL, headers=headers, json=output) # Send the request
	
    # Response tratament
	rr = response.json()
	response = rr[0]["generated_text"]
	response = response.replace("Generated Prompt ", "")
    
	return response # Return the response


# Define the generate function
def generate(inputt):
	# Prompt tratament
	prompt_input = prompt(inputt)
	image_bytes = ({"inputs": prompt_input})
	
	# Response tratament
	response = requests.post(API_URL, headers=headers, json=image_bytes)
	response = response.content
	
	# Save the image
	image = Image.open(io.BytesIO(response))
	image.save("ia\image\generations\generated_image.png")