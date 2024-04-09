import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta 
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
     print("Understanding")
     query = r.recognize_google(audio,language='en-in')
     print(f"You Said: {query}")
    except Exception as e:
     print("Say that again")
     return "None"
    return query  

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("Who do want to text?") 
    speak("For Person 1 say 1")
    speak("For Person 2 say 2")
    a = takeCommand().lower()
    
    if a == "1":
        speak("What is the message?")
        message = str(takeCommand().lower())
        pywhatkit.sendwhatmsg("+919840609379",message,time_hour=strTime,time_min=update)
        
    elif a == "2": 
        pass
    
     