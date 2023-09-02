# Imports
import speech_recognition as sr
import threading

# Modules imports
import database.operations as dbOp
import executor as ex


# Main function to back-end
def main():
    r = sr.Recognizer() # Creating the Speech Recognition and defines the openai key
    response = "none" # Defines the response variable

    # Loop to capture and recognize the sound of the microfone
    with sr.Microphone() as source:
        # Gave fit in the audio to ajust with ambient
        print("->starting audio adjustment<-")
        r.adjust_for_ambient_noise(source, duration=1)
        print("->given fit<-")

        print("initialization...\n")
        while True:
            print("listening...\n")
            try:
                basic_audio = r.listen(source)
                text_audio=(r.recognize_google(basic_audio, language="pt-br"))
                text_audio = text_audio.lower() 
                print("recognizing...\n")
                print(text_audio + "\n")

                # Funcion to get the time
                if dbOp.question("time", text_audio):
                    response = ex.time()
                
                # Funcion to Search something in the internet
                elif dbOp.question("search", text_audio):
                    print("1")

                # Funcion to Activate
                elif dbOp.question("activate", text_audio):
                    if dbOp.question("mode", text_audio): # Funcion to Activate a mode
                        if dbOp.question("chat", text_audio): # Funcion to Activate the chat mode
                            response = ex.chat_mode()


                # Incert a log
                dbOp.log_insert(text_audio, response)
       
            # To unknown values
            except sr.UnknownValueError:
                print("...")


# Interface to put the password and the loggin
if __name__ == "__main__":    
    if True:
        # Starts a thread to the back-end code
        main_thread = threading.Thread(target=main)
        main_thread.start()

    # If the password or the loggin is incorrect the code executes the else
    else:
        exit()