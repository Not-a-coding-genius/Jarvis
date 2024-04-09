import requests
import json
import speech_recognition
import pyttsx3
import os
import requests

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
    
def latestnews():
    apidict = {"business": "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=0d13e895601d4dd2a05c482826ea3692",
               "entertainment":"https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=0d13e895601d4dd2a05c482826ea3692",
                "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=0d13e895601d4dd2a05c482826ea3692",
                "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=0d13e895601d4dd2a05c482826ea3692",
                "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=0d13e895601d4dd2a05c482826ea3692",
                "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=0d13e895601d4dd2a05c482826ea3692"} 
    
    content = None
    url = None
    speak("Choose an area")
    speak("1 Business")
    speak("2 Entertainment")
    speak("3 Health")
    speak("4 Science")
    speak("5 Technology")
    speak("6 Sports")
    
    query = takeCommand().lower()
    for key ,value in apidict.items():
        if key.lower() in query.lower():
            url = value
            print(url)
            print("URL was found")
            break
        else:
            url = True
            if url is True:
                print("URL not found") 
                
    news = requests.get(url).text
    news = json.loads(news)
    speak("Headline One")
    
    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"For more info visit: {news_url}")
        speak("Do you want me to continiue?")
        a = takeCommand().lower()
        if "no" in a:
            break
        else:
            pass

       
            
    
        
        
    
    
       