# Import the Libraries
import io
from PIL import Image
import PIL
import requests
import system.config.operations as op
import system.messages as msg
import random
import modules.sounds.voice as voice


# Define the API URL and the headers
TEXT_API_URL = op.load("system\config\ia.yaml", "prompt_extend")
API_URL = op.load("system\config\ia.yaml", "DucHaiten")
headers = {"Authorization": "Bearer " + op.load("system\config\ia.yaml", "api_token")}


# Define the prompt function
def prompt(input_prompt):
	random_seed = random.randint(0, 50)
	# Prompt tratament
	input_prompt = "Generated Prompt " + input_prompt
	generate_kwargs = dict(
        max_new_tokens=100,
		seed=random_seed,
    )
	
	output = ({"inputs": input_prompt, "parameters": generate_kwargs}) # Define the output
	response = requests.post(TEXT_API_URL, headers=headers, json=output) # Send the request
	
    # Response tratament
	rr = response.json()
	try:
		response = rr[0]
		response = response["generated_text"]
		response = response.replace("Generated Prompt ", "")
		msg.error("Error to Generate the prompt to the image, triyng again with another prompt")
	except:
		try:
			response = rr["generated_text"]
			response = response.replace("Generated Prompt ", "")
			msg.error("Error to Generate the prompt of the image, triyng again with another prompt")
		except:
			response = rr
    
	return response # Return the response


# Define the generate function
def generate(inputt):
	# Prompt tratament
	prompt_input = prompt(inputt)
	image_bytes = ({"inputs": prompt_input})
	
	# Response tratament
	response = requests.post(API_URL, headers=headers, json=image_bytes)
	res = response.content
	
	# Save the image
	try:
		image = Image.open(io.BytesIO(res))
		image.save("ia\image\generations\generated_image.png")
		voice.speak("Image generated with success")
		
		# Open the image
		img = Image.open('ia\image\generations\generated_image.png')
		# Show the image
		img.show()

	except PIL.UnidentifiedImageError:
		msg.error("Received invalid image data from the API")
		voice.speak("I received a invalid image data from the API")