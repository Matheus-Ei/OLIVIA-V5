# Imports
import os
import pygame
from pydub import AudioSegment
from pydub.playback import play
import pyttsx3
import speech_recognition as sr

# Inits the engines
pygame.init() # Init the pygame to reproduces the voice
engine = pyttsx3.init() # Starts the text-speack
r = sr.Recognizer() # Creating the Speach Recognition and defines the openai key


# Function for normal speech, longer, but with better quality
def speak(data):
    # Voices
    voice = 'pt-BR-AntonioNeural'
    voice2 = 'pt-BR-FranciscaNeural'

    # Command Definition
    data = data.replace('\n'," ")
    command = f'edge-tts --rate="+20%" --voice "{voice2}" --text "{data}" --write-media "modules\sounds\data.mp3"'

    os.system(command) # Sends the command to CMD
    
    pygame.mixer.init()
    pygame.mixer.music.load("modules\sounds\data.mp3") # Loads the sound to pygame

    # Try speak the voice
    try:
        pygame.mixer.music.play() 
        print("-> "+data+" <-")
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    # If the code had exeption
    except Exception as e:
        print("The speak code had error, please check the code to correct this exeption: -->")
        print(e)
    
    # Turn off the pygame
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


# Function for fast speech, but with lower quality
def fast_speak(texto):
    print("-> "+texto+" <-")
    
    engine.save_to_file(texto, "modules\sounds\data.mp3")
    engine.setProperty("rate", 300) # Speed Change
    engine.runAndWait() # run the voice

    audio = AudioSegment.from_wav("modules\sounds\data.mp3")
    volume_adjustment = 6 # Adjusts the volume
    audio = audio + volume_adjustment
    play(audio)


# Funcion to Listening the Voice from the User
def listening():
    with sr.Microphone() as source:
        print("->starting audio adjustment<-")
        r.adjust_for_ambient_noise(source, duration=0.2) # Time to ajust the microfone recognition with the sound of the ambient
        print("->given fit<-")
        print("initialization...\n")
        while True:
            print("listening...\n")
            try:
                basicAudio = r.listen(source)
                textAudio=(r.recognize_google(basicAudio, language="pt-br"))
                textAudio = textAudio.lower() 
                print(textAudio)
                return textAudio

            except sr.UnknownValueError:
                print("...")


# To Test the Funcions
if __name__ == "__main__":
    fast_speak("Esse é um teste de voz para saber como está ficando")
    fast_speak("Esse é um teste de voz para saber como está ficando isso")
    fast_speak("como está ficando isso?")