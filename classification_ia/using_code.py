# Import the libraries
from tensorflow.keras.models import load_model
import tokens as tk
import numpy as np

# load model.que
loaded_model = load_model(r'classification_ia\model.h5')

# Start the loop.
while True:
    # Get the input.
    word = input("Digite uma frase: ")
    start_word = [word] # Convert to list
    tokenized_start_word = tk.tokenizing(start_word) # Tokenize the input

    # Convert to numpy array
    tokenized_start_word = np.array(tokenized_start_word) 
    tokenized_start_word = np.array([np.array(tokens) for tokens in tokenized_start_word])

    # Make the prediction.
    predictions = loaded_model.predict(tokenized_start_word) 
    class_predictions = np.argmax(predictions, axis=1) # Get the class with the highest probability

    # Print the prediction.
    print(predictions)
    print(class_predictions)