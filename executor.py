# Imports
from datetime import datetime

# Modules Imports
import modules.sounds.voice as voice
import modules.translator as translator
import database.operations as dbOp
import modules.search as searchf

# IA imports
import ia.chat.bot as bot
import ia.sumarization.sumarizer as sumarizer


# Funcion to get the time
def time():
    time=datetime.now() # Create datatime object
    hour = int(time.strftime("%H")) # Get the hour
    minutes = int(time.strftime("%M")) # Get the minutes
    response = "Agora são %d, e %d minutos!" %(hour ,minutes) # Create the response

    voice.speak(response) # Speak the response
    return response # Return the response


# Funcion to Search something in the internet
def search(text):
    text = translator.translation(text, "pt", "en") # Translate to English
    search_result = searchf.google(text, 1) # Execute the search

    sum_search_result = sumarizer.sumarize(str(search_result)) # Sumarize the search result

    print(sum_search_result)

    sum_search_result = translator.translation(sum_search_result, "en", "pt") # Translate to Portuguese

    voice.speak(sum_search_result) # Speak the response
    return(sum_search_result) # Return the result


# Chatbot Mode Loop
def chat_mode():
    history = [] # Creates Hitory list
    # Funcion to Chat with the bot in Loop
    while True:
        input_prompt = voice.listening() # Listen the user

        if dbOp.question("deactivate", input_prompt):
            if dbOp.question("mode", input_prompt): # Funcion to Activate a mode
                if dbOp.question("chat", input_prompt): # Funcion to Activate the chat mode
                    return "chat" # Return the history
                
        else:
            tra_input_prompt = translator.translation(str(input_prompt), "pt", "en") # Translate to English

            response, history = bot.chatbot(tra_input_prompt, history=history) # Get the response from the bot

            trans_response = response[-1] # Converts the response to get the lasts tuple
            trans_response = trans_response[-1] # Converts the last response on the tuple to string
            trans_response = translator.translation(str(trans_response), "en", "pt") # Translate to Portuguese

            voice.speak(str(trans_response))