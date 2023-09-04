# Importing the libraries
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from keras.layers import Conv1D, GlobalMaxPooling1D, Bidirectional
import numpy as np
import tokens as tk
import pandas as pd
from tensorflow.keras.utils import to_categorical
import module as md


# Funcion to check the number of elements in each class and add more elements to the class with less elements
#md.normalizer(r"ia\classification\datasets\small_dataset.csv")


# Read the dataset File
dataset = pd.read_csv(r'ia\classification\datasets\small_dataset.csv')


# Create the lists of contents and classes.
contents = dataset['text'].tolist()
classes = dataset['class'].tolist()

# Tokenize the text.
x_train = tk.tokenizing(contents)
y_train = classes

# Convert x_train to numpy array.
x_train = np.array(x_train)
x_train = np.array([np.array(tokens) for tokens in x_train]) # Reshape x_train
# Convert y_train to numpy array.
y_train = np.array(y_train)
y_train = y_train.reshape(-1, 1) # Reshape y_train

num_classes = 3 # Define the number of classes.
y_train = to_categorical(y_train, num_classes) # Convert y_train to categorical.

# Print the shapes of x_train and y_train.
print("-------------------")
print(x_train)
print("-------------------")
print(y_train)
print("-------------------")

# Define the model.
model = Sequential()
model.add(Embedding(input_dim=50000, output_dim=128, input_length=x_train.shape[1]))
model.add(LSTM(256, return_sequences=True))  # Use return_sequences=True to sequences of LSTM
model.add(Dropout(0.5))  # Adds a dropout layer to prevent overfitting
model.add(LSTM(128))  # Other LSTM layer
model.add(Dense(num_classes, activation='softmax')) # Output layer with number of classes and softmax activation function


# Compile the model.
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# Train the model.
model.fit(x_train, y_train, epochs=10, batch_size=2, validation_split=0.1)


# Evaluate the model.
loss, accuracy = model.evaluate(x_train, y_train)
print("Loss:", loss)
print("Accuracy:", accuracy)

# Save the model.
model.save('ia\classification\model.h5')