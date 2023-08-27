# Import the libraries
import pandas as pd
from transformers import AutoTokenizer
import numpy as np

# Funcion to tokenize the text.
def tokenizing(array):
    # Defining the variables.
    i=0
    input_ids_return = []
    texto = ""

    # Loop to process all the texts.
    while i<len(array):
        texto = array[i]
        # Load a pre-trained tokenizer
        tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

        # Tokenizing the text
        tokens = tokenizer.tokenize(texto)

        # Padding and Truncating Sequences
        max_length = 5  # Max length of the tokens
        padding = 'max_length'  # Padding the tokens
        padded_tokens = tokenizer(tokens, padding=padding, truncation=True, max_length=max_length, return_tensors="pt")
        input_ids = padded_tokens["input_ids"]

        # Converting to numbers
        input_ids = input_ids[0].numpy()  # Converting to NumPy array
        print("Input IDs (NumPy array):", input_ids)
        input_ids_return.append(input_ids)
        i=i+1

    # Retun the input_ids.
    print(input_ids_return)
    return(input_ids_return)


# Funcion to untokenize the text.
def untokenize(input_ids):
    # Load a pre-trained tokenizer
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

    # Convert Ids to tokens
    tokens_back = tokenizer.convert_ids_to_tokens(input_ids)
    print("Tokens Back:", tokens_back)

    # Untokenizing the text
    texto_destokenizado = tokenizer.convert_tokens_to_string(tokens_back)
    print("Texto destokenizado:", texto_destokenizado)
    return(texto_destokenizado)