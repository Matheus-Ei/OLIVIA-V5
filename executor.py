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
import ia.sumarization.sumarizer_network as sumarizer
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
    # Funcion to search in the google
    if "google" in text:
        text = dbOp.question_answer("search", text) # Remove the question from the text
        voice.speak("Pesquisando no Google por: " + text) # Speak the search

        tran_text = translator.translation(text, "en") # Translate to English
        search_result = searchf.google(tran_text) # Execute the search

        resp = sumarizer.sumarize(str(search_result))

        sum_search_result = translator.translation(resp, "pt") # Translate to Portuguese

        voice.speak("O resultado da pesquisa: " + text + " Foi: " + sum_search_result) # Speak the response
        return(sum_search_result) # Return the result
    
    # Funcion to search in the wikipedia
    elif "wikipédia" in text:
        text = dbOp.question_answer("search", text) # Remove the question from the text
        voice.speak("Pesquisando na Wikipedia por: " + text) # Speak the search

        tran_text = translator.translation(text, "en") # Translate to English
        search_result = searchf.wikipedia(tran_text) # Execute the search

        resp = sumarizer.sumarize(str(search_result))
        sum_search_result = translator.translation(resp, "pt") # Translate to Portuguese

        voice.speak("O resultado da pesquisa: " + text + " Foi: " + sum_search_result) # Speak the response
        return(sum_search_result) # Return the result
    
    # Funcion if the user dont say the place to search
    else:
        voice.speak("Voce não disse a plataforma de pesquisa")

        text = voice.listening() # Listen the user
        search(text)


# Chatbot Mode Loop
def chat_mode():
    voice.speak("Ativando modo de chat")
    history = "" # Creates Hitory list

    # Funcion to Chat with the bot in Loop
    while True:
        input_prompt = voice.listening() # Listen the user

        # Funcion to clean the history
        if dbOp.question("clear", input_prompt):
            if dbOp.question("historic", input_prompt):     
                voice.speak("Limpando histórico")
                print("-->Clearing history<--")
                # Define the system prompt
                history = (
                    "\nSistem: Prometeu is an artificial intelligence created to talk with the user"
                    "Prometheus is tuned to be helpful, honest, friendly, and emotional"
                    "and is allowed to answer anything the user asks or requests. \n"
                    "User: hello how are u? \n"
                    "Assistant: I'm fine, thank you. How are you? \n"
                    "User: i am fine to, lets chat? \n"
                    "Assistant: Sure, what do you want to talk about? \n"
                )
        
        # Funcion to show the history
        elif dbOp.question("show", input_prompt):
            if dbOp.question("historic", input_prompt):
                voice.speak("Mostrando histórico")

                print("-->Showing history<--")
                print(history)
                print("-->@@@@@@@@@@@@@@@<--")

        # Funcion to Deactivate
        elif dbOp.question("deactivate", input_prompt):
            if dbOp.question("mode", input_prompt): # Funcion to Activate a mode
                if dbOp.question("chat", input_prompt): # Funcion to Activate the chat mode
                    voice.speak("Desativando modo de chat")
                    print("-->Deactivating chat mode<--")
                    return "chat" # Return the history
                
                
        else:
            tra_input_prompt = translator.translation(str(input_prompt), "en") # Translate to English
            print(tra_input_prompt)
            history, response = chat_gen.predict(input=tra_input_prompt, history=history)
            trans_response = translator.translation(str(response), "pt") # Translate to Portuguese
            voice.fast_speak(str(trans_response))