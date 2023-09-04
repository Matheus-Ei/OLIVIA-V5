# Imports
print("-->Importing Executor Libraries<--")
from datetime import datetime

# Modules Imports
print("-->Importing Executor Modules<--")
import modules.sounds.voice as voice
import modules.translator as translator
import database.operations as dbOp
import modules.search as searchf

# IA imports
print("-->Importing Executor IA<--")
#import ia.chat.bot as bot
#import ia.sumarization.sumarizer as sumarizer
#import ia.text_gen.gen as text_gen
import ia.text_gen.chat as chat_gen


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
    dbOp.question_answer("search", text) # Remove the question from the text

    text = translator.translation(text, "en") # Translate to English
    search_result = searchf.google(text) # Execute the search
    sum_search_result = sumarizer.sumarize(str(search_result)) # Sumarize the search result
    sum_search_result = translator.translation(sum_search_result, "pt") # Translate to Portuguese

    voice.speak(sum_search_result) # Speak the response
    return(sum_search_result) # Return the result


# Chatbot Mode Loop
def chat_mode():
    voice.speak("Ativando modo de chat")
    history = "" # Creates Hitory list

    # Funcion to Chat with the bot in Loop
    while True:
        input_prompt = voice.listening() # Listen the user

        # Funcion to Deactivate
        if dbOp.question("deactivate", input_prompt):
            if dbOp.question("mode", input_prompt): # Funcion to Activate a mode
                if dbOp.question("chat", input_prompt): # Funcion to Activate the chat mode
                    voice.speak("Desativando modo de chat")
                    print("-->Deactivating chat mode<--")
                    return "chat" # Return the history
                
        # Funcion to clean the history
        if dbOp.question("clear", input_prompt):
            if dbOp.question("historic", input_prompt):     
                voice.speak("Limpando histórico")
                print("-->Clearing history<--")
                history = ""

        # Funcion to show the history
        if dbOp.question("show", input_prompt):
            if dbOp.question("historic", input_prompt):
                voice.speak("Mostrando histórico")

                print("-->Showing history<--")
                print(history)
                print("-->@@@@@@@@@@@@@@@<--")
                
        else:
            tra_input_prompt = translator.translation(str(input_prompt), "en") # Translate to English
            history, response = chat_gen.predict(input=tra_input_prompt, history=history)
            trans_response = translator.translation(str(response), "pt") # Translate to Portuguese
            voice.speak(str(trans_response))