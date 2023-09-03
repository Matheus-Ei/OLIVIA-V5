# Imports
from translate import Translator
from googletrans import Translator


# Funcion to translate the text
def translation(text, from_lan, to_lan):
    print("--> Starting the translate funcion <--")
    text_len = text.__len__() # Get the text length
    if text_len > 499:
        text = text[0:499]

    translator= Translator(from_lang = from_lan, to_lang=to_lan) # Create the translator object
    translation = translator.translate(text) # Translate the text

    print("--> Ending the translate funcion <--")
    return(translation) # Return the translated text


# Google translator
def translation_google(text, lang):
    print("--> Starting the translate funcion <--")
    translater = Translator() # Create the translator object
    
    translation = translater.translate(text, dest=lang) # Translate the text

    print("--> Ending the translate funcion <--")
    return(translation.text) # Return the translated text


