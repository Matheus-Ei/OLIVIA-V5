# Imports
from googletrans import Translator


# Google translator
def translation(text, lang):
    print("--> Starting the translate funcion <--")
    translater = Translator() # Create the translator object
    
    translation = translater.translate(text, dest=lang) # Translate the text

    print("--> Ending the translate funcion <--")
    return(translation.text) # Return the translated text


