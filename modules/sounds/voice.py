# Imports
import os
import pygame
from pydub import AudioSegment
from pydub.playback import play
import pyttsx3
import speech_recognition as sr
import system.messages as msg

# Inits the engines
pygame.init() # Init the pygame to reproduces the voice
engine = pyttsx3.init() # Starts the text-speack
r = sr.Recognizer() # Creating the Speach Recognition and defines the openai key


# Function for fast speech, but with lower quality
def fast_speak(texto):
    # Data treatment
    texto = texto.replace('\n'," ")
    texto = texto.replace('.',",")
    texto = texto.replace('-'," ")

    msg.assistent(texto)
    
    engine.save_to_file(texto, "modules\sounds\data.mp3")
    engine.setProperty("rate", 250) # Speed Change
    engine.runAndWait() # run the voice

    audio = AudioSegment.from_wav("modules\sounds\data.mp3")
    volume_adjustment = 6 # Adjusts the volume
    audio = audio + volume_adjustment
    play(audio)


# Function for normal speech, longer, but with better quality
def speak(data):
    # Voices
    voice = 'pt-BR-AntonioNeural'
    voice2 = 'pt-BR-FranciscaNeural'

    # Data treatment
    data = data.replace('\n'," ")
    data = data.replace('.',",")
    data = data.replace('-'," ")

    # Command Definition
    try:
        command = f'edge-tts --rate="+20%" --voice "{voice2}" --text "{data}" --write-media "modules\sounds\data.mp3"'
        os.system(command) # Sends the command to CMD
    
        pygame.mixer.init()
        pygame.mixer.music.load("modules\sounds\data.mp3") # Loads the sound to pygame

        # Try speak the voice
        try:
            pygame.mixer.music.play() 
            msg.assistent(data)
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        # If the code had exeption
        except Exception as e:
            msg.error("The Speak Code Had a Error: " + str(e))

        # Turn off the pygame
        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()

    # if cant speak the voice with the voice2, try with the voice fast speak
    except:
        fast_speak(data)
    

# Funcion to Listening the Voice from the User
def listening():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1) # Time to ajust the microfone recognition with the sound of the ambient
        while True:
            msg.continuation("Listening")
            try:
                basicAudio = r.listen(source)
                textAudio=(r.recognize_google(basicAudio, language="pt-br"))
                textAudio = textAudio.lower() 
                msg.user(textAudio)
                return textAudio

            except sr.UnknownValueError:
                msg.error("Unknown Value Error")


# To Test the Funcions
if __name__ == "__main__":
    fast_speak("Esse é um teste de voz para saber como está ficando")
    fast_speak("Esse é um teste de voz para saber como está ficando isso")
    fast_speak("como está ficando isso?")