# Import the Libraries
from transformers import AutoTokenizer, BartForConditionalGeneration

# Load the model and tokenizer
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

# Funcion to sumarize the text
def sumarize(text):
    print("--> Starting the sumarize funcion <--")
    text = text.replace("\n", "") # Remove the \n
    text = text.replace("\t", "") # Remove the \t
    text = text.replace("\r", "") # Remove the \r
    text = text.replace('"', "") # Remove the "
    text = text.replace("'", "") # Remove the '
    text = text.replace("”", "") # Remove the ”
    text = text.replace("“", "") # Remove the “
    text = text.replace("(", "") # Remove the (
    text = text.replace(")", "") # Remove the )
    text = text.replace("[", "") # Remove the [
    text = text.replace("]", "") # Remove the ]
    text = text.replace("{", "") # Remove the {
    text = text.replace("}", "") # Remove the }
    text = text.replace(":", "") # Remove the :
    text = text.replace(";", "") # Remove the ;
    text.lower() # Convert to lower case
    
    inputs = tokenizer([text], max_length=1000000, return_tensors="pt", truncation=True) # Create a input object and tokenize

    summary_ids = model.generate(inputs['input_ids'], num_beams=10, min_length=10, max_length=1000000) # Generate Summary
    ret = tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0] # Detokenize and convert to string

    print("--> Ending the sumarize funcion <--")
    return ret