# Imports
from datetime import datetime

# Freatures Imports
import freatures.sounds.voice as voice


# Funcion to get the time
def time():
    time=datetime.now() 
    hour = int(time.strftime("%H"))
    minutes = int(time.strftime("%M"))
    response = "Agora são %d, e %d minutos!" %(hour ,minutes)

    voice.speak(response)
    return response