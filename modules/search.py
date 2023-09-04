# Import the Libraries
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import ia.sumarizer as sumarizer
import wikipediaapi


# Funcion to search in the google
def google(query):
    # to seartch in the google
    print("--> Starting the google search funcion <--")
    for url_text in search(query, num_results=1, timeout=1):
        response = requests.get(url=url_text)

        print("--> Getting the text from the url: " + url_text + " <--")
        soup = BeautifulSoup(response.content, 'html.parser') # Parse the HTML content with BeautifulSoup

        # Extract the information on paragraphs
        paragraphs = [p.get_text() for p in soup.find_all('p')]

        # Join the paragraphs
        text = " "
        i=0
        for p in paragraphs:
            if i > 10:
                print("--> i>10 <--")
                print("--> Ending the google search funcion <--")
                return(text) # Return the text
            
            elif i > 1:
                p = sumarizer.sumarize(str(p))
                text = str(text) + " " + str(p)
            i=i+1

        print("--> Ending the google search funcion <--")
        return(text) # Return the text
    


# Funcion to search in the wikipedia
def wikipedia(query):
    # to seartch in the wikipedia
    print("--> Starting the wikipedia search funcion <--")

    # Creates a wikipedia object
    wiki_wiki = wikipediaapi.Wikipedia('pt')
    page_py = wiki_wiki.page(query)

    # Verify if the page exists
    if page_py.exists():
        print("--> Título da Pagina: %s <--" % page_py.title) # Print the title of the page
        a=page_py.text # Gets the text of the page
        return(a) 

    else:
        print("A página não foi encontrada.")
        return("A página não foi encontrada.")

    print("--> Ending the wikipedia search funcion <--")



