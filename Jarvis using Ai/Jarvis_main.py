import pyttsx3
import speech_recognition
import requests
import bs4
#import BeautifulSoup
import html.parser
import datetime
import pyautogui
import os
import keyword
import random
import webbrowser
from plyer import notification



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

for i in range(3):
    a = takeCommand().lower()
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if(a==pw):
        speak("WELCOME BACK")
        speak("wake me up")
        break
    elif(i==2 and a!=pw):
        exit()
    
    elif (a!=pw):
        speak("Try Again")    




if __name__ == "__main__" :
    while True: 
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
            
            while True: 
                query = takeCommand().lower()
                if "go to sleep" in query: 
                    speak("Okay Ma'am, You can call me anytime")
                    break
                
                elif "change password" in query:
                    speak("What's the new password?")
                    new_pw = takeCommand().lower()
                    new_password=open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done")
                    speak(f"Your new password is {new_pw}")
                    
                elif "schedule my day" in query:
                    tasks = [] #empty list
                    speak("Do you want to clear the previous schedule?")
                    speak("Say yes to clear")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        speak("Please tell the number of tasks")
                        no_tasks = takeCommand().lower()
                        i = 1
                        for i in range(int(no_tasks)):
                         speak("Please tell the task")
                         tasks.append(takeCommand().lower())
                         file = open("tasks.txt","a")
                         file.write(f"{i}. {tasks[i]}\n")
                         file.close()
                              
                    elif "no" in query: 
                            i = 1
                            for i in range(int(no_tasks)):
                                speak("Please tell the task")
                                tasks.append(takeCommand().lower())
                                file = open("tasks.txt","a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                elif "what is my schedule" in query:
                        file = open("tasks.txt","r")
                        content = file.read()
                        speak(content)
                        file.close()
                        notification.notify (
                        title = "My schedule:- ",
                        message = content,
                        timeout = 30
                    ) 
                elif "hello" in query: 
                    speak("Hello ma'am, how are you doing?")
                     
                elif "I am fine" in query:
                    speak("That's great!")
                     
                elif "How are you?" in query:
                    speak("I'm doing good")
                     
                elif "thank you" in query:
                    speak("You are welcome, ma'am")
                
                elif "tired" in query:
                    speak("Playing your favourite songs")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=gWdjDwYuejI&list=PLBDkiF2p81Gl59Mz1Kjmaf9kIh2KAEa7z")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=pQtJQFoCO8U") 
                    elif b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=OuTLKgPyaF0")       
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")    
                
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video playing")
                
                elif "mute" in query: 
                    pyautogui.press("m")
                    speak("video muted")
                    
                elif "volume up" in query: 
                   from keyboard import volumeup
                   speak("turning volume up")
                   volumeup()
                   
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("turning volume down")
                    volumedown()
                                    
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                    
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)        
                
                elif "google" in query:
                    from  SearchNow import searchGoogle
                    searchGoogle(query)    
                
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia   
                    searchWikipedia(query)    
                    
                elif "news" in query: 
                    from NewsRead import latestnews
                    latestnews()   
                
                elif "calculate"  in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                    
                elif "whatsapp" in query: 
                    from Whatsapp import sendMessage
                    sendMessage()
                    
                elif "shutdown the system" in query:
                    speak("To shut down the system say yes")
                    shutdown = takeCommand().lower()
                    if shutdown == "yes" :
                        os.system("shutdown /s /t 1")
                        
                    elif shutdown == "no":
                        break
                        
                
                elif "temperature" in query:
                    search = "temperture in Chennai"
                    url = f"https://www.google.com/search?q={search}"    
                    r = requests.get(url)
                    from bs4 import BeautifulSoup
                    from html.parser import HTMLParser
                    class HTMLParser(HTMLParser):
                        def handle_starttag(self, tag, attrs):
                            print("Encountered a start tag:", tag)

                        def handle_endtag(self, tag):
                            print("Encountered an end tag :", tag)

                        def handle_data(self, data):
                            print("Encountered some data  :", data)

                        parser = HTMLParser()
                        parser.feed('<html><head><title>Test</title></head>'
                        '<body><h1>Parse me!</h1></body></html>')
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe" ).text
                    speak(f"current{search} is {temp}")
                
                elif "weather" in query:
                    search = "temperature in Chennai"
                    url = f"https://www.google.com/search?q={search}"    
                    r = requests.get(url)
                    from bs4 import BeautifulSoup
                    from html.parser import HTMLParser
                    class HTMLParser(HTMLParser):
                        def handle_starttag(self, tag, attrs):
                            print("Encountered a start tag:", tag)

                        def handle_endtag(self, tag):
                            print("Encountered an end tag :", tag)

                        def handle_data(self, data):
                            print("Encountered some data  :", data)

                        parser = HTMLParser()
                        parser.feed('<html><head><title>Test</title></head>'
                        '<body><h1>Parse me!</h1></body></html>')
                    
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe" ).text
                    speak(f"current{search} is {temp}")        
                    
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Ma'am the time is {strTime}")
                
                elif "shutdown" in query: 
                    speak("Shutting Down")
                    exit()    
                
                elif "remember that" in query: 
                    rememberMessage = query.replace("remember that","")    
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","w")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())    
                    
                            
                
                
    
            