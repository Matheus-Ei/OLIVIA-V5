# Import the Libraries
from random import randint
import pandas as pd
import csv

def normalizer(dataset_name):
    # Funcion to check the number of elements in each class and add more elements to the class with less elements
    def check_elements():   
        # Read the dataset File
        dataset = pd.read_csv(dataset_name)


        # Create the lists of contents and classes.
        text = dataset['text'].tolist()
        classes = dataset['class'].tolist()

        i=0
        num_classes_array = []
        unique_classes = 0
        num_classes = 0

        # Counts how many diferent classes have in the dataset
        unique_classes = set(classes)
        unique_classes = len(unique_classes)

        # Counts how many diferent elements have in each class
        while i < unique_classes:
            num_classes = classes.count(i)
            print(num_classes)

            # Array that contains the number of elements in each class in order
            num_classes_array.append(num_classes)

            i = i + 1

        return num_classes_array, unique_classes, text, dataset

    num_classes_array, unique_classes, text, dataset = check_elements()


    # Gets the class with more elements
    max_class = max(num_classes_array)
    print("Classe maior: " + str(max_class))


    # Adds more elements in the class with less elements
    ii=0
    while ii < unique_classes:
        if num_classes_array[ii] < max_class:
            
            # adiciona uma linha dentro do dataset para a classe com menos elementos
            random_number = randint(0, num_classes_array[ii]-1)

            ele_class = dataset[dataset['class'] == ii]
            ele_class = ele_class['text'].tolist()

            # add a line to the dataset
            with open(dataset_name, 'a', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['text', 'class'])
                writer.writerow({'text': ele_class[random_number], 'class': ii})


            print('adding line to class: ' + str(ii))
            
        else:
            print('---->> ok <<----')
            ii = ii + 1

        num_classes_array, unique_classes, text, dataset = check_elements()
