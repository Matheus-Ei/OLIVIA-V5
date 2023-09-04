# Libraries Imports
import numpy as np
from tensorflow.keras.models import load_model

# Modules imports
import tokens as tkn


# Starting the classification IA
print("->starting classifier<-")
# Using the classification IA
loaded_model = load_model(r'ia\classification\model.h5') # load model.
print("->classifier started<-")


def use(text_audio):
    # Tokenize the input
    array_ta = [text_audio] # Convert to list
    tokenized_start_word = tkn.tokenizing(array_ta) # Tokenize the input

    # Convert to numpy array
    tokenized_start_word = np.array(tokenized_start_word) 
    tokenized_start_word = np.array([np.array(tokens) for tokens in tokenized_start_word])

    # Make the prediction.
    predictions = loaded_model.predict(tokenized_start_word) 
    class_predictions = np.argmax(predictions, axis=1) # Get the class with the highest probability

    # Print the prediction.
    print("--===<Prediction Prob>===--")
    print(predictions)
    print("--===:::===--\n")

    print("--===<Class Predicted>===--")
    print(class_predictions)
    print("--===:::===--")

    cp = class_predictions
    return cp