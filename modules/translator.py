# Imports
from translate import Translator

# Funcion to translate the text
def translation(text, from_lan, to_lan):
    translator= Translator(from_lang = from_lan, to_lang=to_lan) # Create the translator object
    translation = translator.translate(text) # Translate the text

    return(translation) # Return the translated text