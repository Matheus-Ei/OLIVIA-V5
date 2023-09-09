# Modules Imports
import modules.sounds.voice as voice
import modules.search as searchf
import system.messages as msg
import modules.spotify as spotify
import modules.messages as messages
msg.informative("Executor Modules Imported")

# Imports
import colorama
from datetime import datetime
from PIL import Image
msg.informative("Default Executor Libraries Imported")

# IA imports
import ia.sumarizer as sumarizer
import ia.questions as questions
import ia.image.image as image_gen
msg.informative("AI Executor Imported")


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
    tran_text = questions.response("What do I want to search on the internet?", text) # To discover what the user want to search
    voice.speak("Searching on Google for: " + tran_text) # Speak the search

    search_result = searchf.google(tran_text) # Execute the search
    resp = sumarizer.sumarize(str(search_result)) # Sumarize the result

    voice.speak("The search result of " + text + " was: " + resp) # Speak the response
    return(resp) # Return the result
    

# Funcion to generate a image
def generate_image(text):
    text = questions.response("What image I want to generate?", text) # To discover what the user want to search
    voice.speak("Generating a image of: " + str(text)) # Speak the search
    image_gen.generate(text) # Generate the image
    return("Generating a image of: " + str(text))


# Funcion to play music
def play_music():
    song = spotify.play() # Play the music
    voice.speak(song)
    return(song)


# Funcion to jump the music
def next_music():
    song = spotify.next() # Jump the music
    voice.speak(song)
    return(song)


# Funcion to pause the music
def pause_music():
    song = spotify.pause() # Pause the music
    voice.speak(song)
    return(song)


# Funcion to select the music
def select_music(text):
    inputt = questions.response("What music do i want to play?", text) # To discover what the user want to search
    song = spotify.select(inputt) # Select the music
    voice.speak(song)
    return song


# Funcion to send a whatsapp message
def send_whatsapp_message(text):
    ret = messages.whatsapp(text)
    return ret