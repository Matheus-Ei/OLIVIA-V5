# Imports
import speech_recognition as sr
import threading
import numpy as np
from tensorflow.keras.models import load_model


# Freatures imports
import classification_ia.tokens as tk
import database.operations as database_op

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


                # Using the classification IA
                loaded_model = load_model(r'classification_ia\model.h5') # load model.

                array_ta = [text_audio] # Convert to list
                tokenized_start_word = tk.tokenizing(array_ta) # Tokenize the input

                # Convert to numpy array
                tokenized_start_word = np.array(tokenized_start_word) 
                tokenized_start_word = np.array([np.array(tokens) for tokens in tokenized_start_word])

                # Make the prediction.
                predictions = loaded_model.predict(tokenized_start_word) 
                class_predictions = np.argmax(predictions, axis=1) # Get the class with the highest probability

                # Print the prediction.
                print("--===<Prediction Prob>===--")
                print(predictions)
                print("--===:::===--\n")

                print("--===<Class Predicted>===--")
                print(class_predictions)
                print("--===:::===--")
                cp = class_predictions


                if cp == 0:
                elif cp == 1:
                elif cp == 2:



            database_op.log_insert(text_audio, response)
       
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