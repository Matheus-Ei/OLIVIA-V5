# Import the Libraries
from googlesearch import search
import requests
from bs4 import BeautifulSoup


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
        for p in paragraphs:
            text = text + " " + p
        
        print("--> Ending the google search funcion <--")
        return(text) # Return the text