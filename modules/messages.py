# Import the libraries
import pywhatkit as kit
import time
import pyautogui
import pygetwindow as gw
import system.messages as msg
import modules.sounds.voice as voice
import ia.questions as questions
import modules.translator as translator
import modules.sounds.audios as audios
import ia.message_separation as message_separation

# Send a whatsapp message
def whatsapp(text):
    # Get the contacts number
    dicionary = {
        "mom": "63 9985-0556",
        "dad": "63 9919-0929",
        "sister": "55 9937-2808",
        "giovanna": "55 9937-2808",
        "luigi": "49 9988-0570",
        "victor": "49 9148-1108",
    }
    people = questions.response("Who do I want to send the message to?", text) # To discover who the user want to send the message
    try:
        number = dicionary[f"{people}"]
    except:
        voice.speak("I fall to find this person in my contacts")
        return("I fall to find this person in my contacts")
    country_code = "+55"

    message = message_separation.predict(text)
    trans_message = translator.translation(message, "pt")

    voice.speak(f"do you realy want to send this message '{message}' to '{people}'?")
    audios.play(r"modules\sounds\default_voices\if_yes_say_yes.mp3")
    msg.continuation("if yes say yes")
    res = voice.listening()

    if "yes" in res:
        kit.sendwhatmsg_instantly(f"{country_code}{number}", trans_message, wait_time=8)
        
        time.sleep(0.5)  # Atraso para dar tempo de o WhatsApp abrir e a mensagem ser digitada
        pyautogui.click()
        
        time.sleep(0.5)  # Atraso para dar tempo de o WhatsApp abrir e a mensagem ser digitada
        pyautogui.press('enter')

        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')

        voice.speak("Message Sent")
        return(f"Message {message} sent to {people}")
    
    else:
        audios.play(r"modules\sounds\default_voices\message_not_sent.mp3")
        msg.informative("Message not sent")
        return("Message not sent")