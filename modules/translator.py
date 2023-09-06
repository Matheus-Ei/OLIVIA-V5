# Imports
from googletrans import Translator
import system.messages as msg


# Google translator
def translation(text, lang):
    try:
        text = str(text) # Convert the text to string
        msg.informative("Translate Funcion")
        translater = Translator() # Create the translator object
        
        translation = translater.translate(text, dest=lang) # Translate the text
        
        return(translation.text) # Return the translated text
    
    except:
        msg.error("Error to translate the text")



