# Imports
from googletrans import Translator
import system.messages as msg


# Google translator
def translation(text, lang):
    text = str(text) # Convert the text to string
    msg.informative("Starting the Translate Funcion")
    translater = Translator() # Create the translator object
    
    translation = translater.translate(text, dest=lang) # Translate the text

    msg.informative("Ending the Translate Funcion")
    
    return(translation.text) # Return the translated text


