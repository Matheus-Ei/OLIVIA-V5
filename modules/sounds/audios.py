# Imports
import pygame
from pydub import AudioSegment
from pydub.playback import play

# Inits the engines
pygame.init() # Init the pygame to reproduces the voices


# Function for normal speech, longer, but with better quality
def play(name):
    # Command Definition
    pygame.mixer.init()
    pygame.mixer.music.load(name) # Loads the sound to pygame

    # Try speak the voice
    try:
        pygame.mixer.music.play() 
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    # If the code had exeption
    except Exception as e:
        print("The Play Code Had a Error: " + str(e))

    # Turn off the pygame
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

