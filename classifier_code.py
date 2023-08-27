# Imports
import speech_recognition as sr
import threading


# Main function to back-end
def main():
    r = sr.Recognizer() # Creating the Speech Recognition and defines the openai key

    # Loop to capture and recognize the sound of the microfone
    with sr.Microphone() as source:
        # Gave fit in the audio to ajust with ambient
        print("->starting audio adjustment<-")
        r.adjust_for_ambient_noise(source, duration=2)
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

                #Add the conversation to logs
                db.logs(text_audio, text_response)
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