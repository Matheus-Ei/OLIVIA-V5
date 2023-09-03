# Imports the Libraries
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import torch


# Load the model and the tokenizer
tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill",add_cross_attention=False)


# Funcion to filter the last 128 tokens
def take_last_tokens(inputs, note_history, history):
    #Filter the last 128 tokens
    if inputs['input_ids'].shape[1] > 128:
        inputs['input_ids'] = torch.tensor([inputs['input_ids'][0][-128:].tolist()])
        inputs['attention_mask'] = torch.tensor([inputs['attention_mask'][0][-128:].tolist()])
        note_history = ['</s> <s>'.join(note_history[0].split('</s> <s>')[2:])]
        history = history[1:]

    return inputs, note_history, history


# Funcion to add a note to the historical information
def add_note_to_history(note, note_history):
    #Add a note to the historical information
    note_history.append(note)
    note_history = '</s> <s>'.join(note_history)
    return [note_history]


# The chatbot function
def chatbot(message, history):
    print("history: ", history)
    history = history or []
    if history: 
        history_useful = ['</s> <s>'.join([str(a[0])+'</s> <s>'+str(a[1]) for a in history])]
    else:
        history_useful = ["hello, my name is matheus eickhoff</s> <s> hello my name is promet.eu, but you can call me your personal assistent</s> <s>hey assistent how are you?</s> <s> I'm doing well, thank you."]
    
    history_useful = add_note_to_history(message, history_useful)
    
    inputs = tokenizer(history_useful, return_tensors="pt")
    inputs, history_useful, history = take_last_tokens(inputs, history_useful, history)
    
    reply_ids = model.generate(**inputs)
    response = tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
    history_useful = add_note_to_history(response, history_useful)
    
    
    list_history = history_useful[0].split('</s> <s>')
    history.append((list_history[-2], list_history[-1]))
    
    return history, history # Return the history