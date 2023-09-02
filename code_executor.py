# Imports
from datetime import datetime

# Modules Imports
import modules.sounds.voice as voice
import modules.translator as translator

# IA imports
import ia.chat.bot as bot


# Funcion to get the time
def time():
    time=datetime.now() # Create datatime object
    hour = int(time.strftime("%H")) # Get the hour
    minutes = int(time.strftime("%M")) # Get the minutes
    response = "Agora são %d, e %d minutos!" %(hour ,minutes) # Create the response

    voice.speak(response) # Speak the response
    return response # Return the response


# Chatbot Mode Loop
def chat_mode():
    history = [] # Creates Hitory list

    # Funcion to Chat with the bot in Loop
    while True:
        input_prompt = voice.listening() # Listen the user

        if "desativar" in input_prompt:
            return history # Return the history
        else:
            tra_input_prompt = translator.translation(str(input_prompt), "pt", "en") # Translate to English

            response, history = bot.chatbot(tra_input_prompt, history=history) # Get the response from the bot

            trans_response = response[-1] # Converts the response to get the lasts tuple
            trans_response = trans_response[-1] # Converts the last response on the tuple to string
            trans_response = translator.translation(str(trans_response), "en", "pt") # Translate to Portuguese

            voice.speak(str(trans_response))