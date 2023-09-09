# Modules imports
import system.messages as msg
import executor as ex
import modules.sounds.voice as voice
import modules.sounds.audios as audios
import database.operations as db
audios.play(r"modules\sounds\audios\init_process.mp3") # Audio to inform that the process is starting
msg.informative("Modules Imported")
audios.play(r"modules\sounds\default_voices\the_modules_were_imported.mp3")

# Imports Libraries
import speech_recognition as sr
import time
msg.informative("Default Libraries Imported")
audios.play(r"modules\sounds\default_voices\standard_libraries_were_imported.mp3")

# Import IAs
import ia.chat.chat as chat
import ia.classification as classification
msg.informative("IAs Imported")
audios.play(r"modules\sounds\default_voices\artificial_intelligences_were_imported.mp3")


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
        
        seconds = 120 # Define the seconds to count
        counted_time_1 = int(time.time()) # Get the seconds since the epoch
        counted_time_2 = 0
        i_time = 0

        audios.play(r"modules\sounds\audios\olivia_is_online.mp3")
        audios.play(r"modules\sounds\default_voices\olivia_is_online.mp3")

        while True:
            msg.continuation("Listening")
            try:
                basic_audio = r.listen(source)
                text_audio=(r.recognize_google(basic_audio, language="en-us"))
                text_audio = text_audio.lower() 
                msg.continuation("Recognizing")
                msg.user(text_audio)

                
                # To wake up the assistent
                if "olivia" in text_audio:
                    i_time = 0
                    # Get the seconds since the epoch
                    counted_time_1 = int(time.time())
                    audios.play(r"modules\sounds\audios\beep_activate_olivia.mp3")


                # To check if the assistent is awake
                if counted_time_2-counted_time_1 < seconds:
                    # Chatbot part
                    task = classification.predict(text_audio) # Predict the task
                    msg.informative(task)

                    #Funcion to Speak Time
                    if "ASKING_SCHEDULE" in task:
                        ex.time()

                    # Funcion to Search
                    elif "SEARCH_ON_GOOGLE" in task:
                        ex.search(text_audio)

                    # Funcion to Generate Image
                    elif "GENERATE_IMAGE" in task:
                        response = ex.generate_image(text_audio)

                    # Funcion to Play Music
                    elif "PLAY_MUSIC" in task:
                        response = ex.play_music()

                    # Funcion to Jump the Music
                    elif "NEXT_MUSIC" in task:
                        response = ex.next_music()

                    # Funcion to Pause the Music
                    elif "PAUSE_MUSIC" in task:
                        response = ex.pause_music()

                    # Funcion to Select the Music
                    elif "SELECT_MUSIC" in task:
                        response = ex.select_music(text_audio)

                    # Funcion to Send Whatsapp Message
                    elif "SEND_WHATSAPP_MESSAGE" in task:
                        response = ex.send_whatsapp_message(text_audio)
                    

                    # Funcion to Talk with the assistent
                    else:
                        response = chat.predict(text_audio) # Predict the response
                        voice.speak(response) # Speak the response


                    # Incert a log
                    msg.waring("Inserting a Log")
                    db.log_insert(text_audio, response)

                # To waring that Olivia is sleeping
                else:
                    msg.waring("Olivia is sleeping")
                    if i_time == 0:
                        audios.play(r"modules\sounds\audios\beep_desactivate_olivia.mp3")
                        i_time = 1
       
            # To unknown values
            except sr.UnknownValueError:
                msg.error("Unknown Value Error")
            
            # To get the time passed
            finally:
                # Get the seconds since the epoch
                counted_time_2 = int(time.time())


# Interface to put the password and the loggin
if __name__ == "__main__":    
    if True:
        # Starts a thread to the back-end code
        main()