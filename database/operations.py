# Imports
import pyodbc
import random
from datetime import datetime, timedelta
import mysql.connector

# Connection Configs
db_config = {
    "host": "108.167.151.99",
    "user": "finflo09_matheus_db",
    "password": "123@Matheuse",
    "database": "finflo09_prometeu"
}

# Creating the connection with the database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Funcion to insert logs with database
def log_insert(question, response):
    # Gets the data and the time
    time=datetime.now() 
    hour = int(time.strftime("%H"))
    minutes = int(time.strftime("%M"))
    seconds = time.strftime("%S")
    day = time.strftime("%d")
    week = time.strftime("%A")
    mounth = time.strftime("%B")
    year = time.strftime("%Y")

    # Converts the data and the time into string
    year = str(year)
    mounth = str(mounth)
    week = str(week)
    day = str(day)
    hour = str(hour)
    minutes = str(minutes)
    seconds = str(seconds)

    response = str(response)
    question = str(question)

    # Try execute and commit the operation
    try:
        date = str(year+"/"+mounth+"/"+day+":"+week+"/"+hour+":"+minutes+":"+seconds) # Defines the date

        cursor.execute("INSERT INTO logs(usuario, prometeu, data) VALUES ('"+question+"','"+response+"','"+date+"');") # Execute the operation

        conn.commit() # Save the alterations in the logs tabble

    # If haves a exeption the code prints what exeption have
    except pyodbc.Error as e:
        print("The connection with the database to insert logs had one error: -->")
        print(e)


if __name__ == "__main__":
    log_insert("test", "test")