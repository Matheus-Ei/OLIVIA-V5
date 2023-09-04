# Imports
import pyodbc
from datetime import datetime


# Connection Configs
conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=database\data.accdb;'
conn = pyodbc.connect(conn_str)
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
        cursor.execute("INSERT INTO logs (user, response, data) VALUES ('"+question+"', '"+response+"', '"+date+"');") # Execute the operation
        conn.commit() # Save the alterations in the logs tabble

    # If haves a exeption the code prints what exeption have
    except pyodbc.Error as e:
        print("The connection with the database to insert logs had one error: -->")
        print(e)


# Funcion to Check if the question is in the Database
def question(funcion, text):
    try:
        # Execute a consult
        cursor.execute('SELECT question FROM classification WHERE funcion = '+"'"+funcion+"';")
        # Recover the consult data
        rows = cursor.fetchall()
        for row in rows:
            roww = str(row[0])
            if roww in text:
                return True
    except pyodbc.Error as e:
        print(e)


# Funcion to consult the questions to assistent and check if they are in database
def question_answer(funcion, text):
    try:
        # Execute a consult
        cursor.execute('SELECT question FROM classification WHERE funcion = '+"'"+funcion+"';")
        # Recover the consult data
        rows = cursor.fetchall()
        for row in rows:
            roww = str(row[0])
            if roww in text:
                text = text.replace(roww, "")
                return text
    except pyodbc.Error as e:
        print(e)