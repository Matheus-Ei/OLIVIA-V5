# Imports
import colorama
print(colorama.Fore.GREEN + "--> Importing Libraries <--" + colorama.Fore.RESET)
import speech_recognition as sr
import threading

# Modules imports
print(colorama.Fore.GREEN + "--> Importing Modules <--" + colorama.Fore.RESET)
import database.operations as dbOp
import executor as ex
import system.messages as msg
import modules.sounds.voice as voice
import modules.translator as translator


import ia.chat as chat


# Main function to back-end
def main():
    r = sr.Recognizer() # Creating the Speech Recognition and defines the openai key
    response = "none" # Defines the response variable

    # Loop to capture and recognize the sound of the microfone
    with sr.Microphone() as source:
        # Gave fit in the audio to ajust with ambient
        msg.waring("Starting Audio Adjustment")
        r.adjust_for_ambient_noise(source, duration=1)
        msg.informative("Given Fit")

        msg.continuation("Initialization")
        while True:
            msg.continuation("Listening")
            try:
                basic_audio = r.listen(source)
                text_audio=(r.recognize_google(basic_audio, language="pt-br"))
                text_audio = text_audio.lower() 
                msg.continuation("Recognizing")
                msg.user(text_audio)


                # Chatbot part
                history = ""
                tra_input_prompt = translator.translation(str(text_audio), "en") # Translate to English
                history, response, intent = chat.predict(tra_input_prompt, history) # Predict the response
                trans_response = translator.translation(str(response), "pt") # Translate to Portuguese
                voice.speak(trans_response) # Speak the response


                #Funcion to Speak Time
                if "speak_time" in intent:
                    ex.time()


                # Funcion to Search
                elif "search_on_google" in intent:
                    ex.search(text_audio)


                # Incert a log
                msg.waring("Inserting a Log")
                #dbOp.log_insert(text_audio, response)
       
            # To unknown values
            except sr.UnknownValueError:
                msg.error("Unknown Value Error")


# Interface to put the password and the loggin
if __name__ == "__main__":    
    if True:
        # Starts a thread to the back-end code
        main_thread = threading.Thread(target=main)
        main_thread.start()