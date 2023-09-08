# Imports
import colorama
print(colorama.Fore.GREEN + "--> Importing Executor Libraries <--" + colorama.Fore.RESET)
from datetime import datetime
from PIL import Image


# Modules Imports
print(colorama.Fore.GREEN + "--> Importing Executor Modules <--" + colorama.Fore.RESET)
import modules.sounds.voice as voice
import modules.search as searchf
import system.messages as msg

# IA imports
msg.informative("Importing Executor IA")
import ia.sumarizer as sumarizer
import ia.questions as questions
import ia.image.image as image_gen


# Funcion to get the time
def time():
    time=datetime.now() # Create datatime object
    hour = int(time.strftime("%H")) # Get the hour
    minutes = int(time.strftime("%M")) # Get the minutes
    response = "Now it's %d and %d minutes!" %(hour ,minutes) # Create the response

    voice.speak(response) # Speak the response
    return response # Return the response


# Funcion to Search something in the internet
def search(text):
    # Funcion to search in the wikipedia
    if "wikipédia" in text:
        tran_text = questions.response("What do I want to search on the internet?", text) # To discover what the user want to search
        voice.speak("Searching on Wikipedia for: " + tran_text) # Speak the search

        search_result = searchf.wikipedia(text) # Execute the search
        resp = sumarizer.sumarize(str(search_result)) # Sumarize the result

        voice.speak("The search result of " + text + " was: " + resp) # Speak the response
        return(resp) # Return the result
    
    # Funcion if the user dont say the place to search to search in the google
    else:
        tran_text = questions.response("What do I want to search on the internet?", text) # To discover what the user want to search
        voice.speak("Searching on Google for: " + tran_text) # Speak the search

        search_result = searchf.google(tran_text) # Execute the search
        resp = sumarizer.sumarize(str(search_result)) # Sumarize the result

        voice.speak("The search result of " + text + " was: " + resp) # Speak the response
        return(resp) # Return the result
    

# Funcion to generate a image
def generate_image(text):
    try:
        text = questions.response("What image I want to generate?", text) # To discover what the user want to search
        voice.speak("Generating a image of: " + text) # Speak the search
        image_gen.generate(text) # Generate the image
        voice.speak("The image was generated with success!") # Speak the search

        # Open the image
        imagem = Image.open('ia\image\generations\generated_image.png')
        # Show the image
        imagem.show()
        
    except:
        voice.speak("Sorry, I can't generate the image") # Speak the search

