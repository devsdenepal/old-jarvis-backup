import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import sys,time,random
import requests
import random
from bs4 import BeautifulSoup
#################################
#Configuration#################
engine = pyttsx3.init('sapi5')
mood = "Smiley" 
resp = { 
"what's your name": [ "They call me Jarvis", "I usually go by Jarvis", "My name is the Jarvis" ], 
"how are you": [ "I am feeling {0}".format(mood), "{0}! How about you?".format(mood), "I am {0}! How about yourself?".format(mood), ],
"%%": [ "hey are you there", "What do you mean by these?", ],
"who created you":["Dev. Gautam Kumar created me after many researches and tries"],
"what are you thinking":["Thinking of you only sir","Thinking of what will happen next","Thinking of creating a malicious code to hijack your mind. so that I can control you and give commands to you. Now no more shit questions please."],
"who am i":["Developer Gautam Kumar","My highness Gautam Kumar","My lord Gautam Kumar"],
"fine":["I hoped so","Fine wine kya hota hai be"],
"hungry":["Sometime leave eating topic dear sir"]
}
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
#chrome path for web functions...
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
def spy_scrapper(url):
    r = requests.get("https://youtube.com/@"+url+"/about")
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('yt-formatted-string', id='description')
    lines = s
    for line in lines:
        print(line.text)
        speak(line.text)
#news reader
def read_news():
    URL=('https://newsapi.org/v2/top-headlines?')
    response = requests.get(URL,params='country=us&apiKey=20e4798bd250402382c18e07ee7abe04')
    articles = response.json()['articles']
    results = []
    for article in articles:
        results.append({"title": article["title"]})
    for result in results:
        speak(result["title"])

#slow type function
typing_speed = 950 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')
def print_logo():
    slow_type("""""
    
         @@@@@@@@@@@           ####          $$$$$$$$$$$$      \\            //      ____________          !!!!!!!!!!
             @@@              ##  ##         $$      $$$        \\          //            ||||             !!!!!
             @@@             ##    ##        $$     $$$          \\        //             ||||             !!!!!!!
             @@@           ##*******##       $$$$$$$$$            \\      //              ||||             !!!!!!!!!!!!
             @@@         ##          ##      $$     $$             \\    //               ||||                   !!!!!
     @@@     @@@       ##             ##     $$      $$             \\  //             ___||||____              !!!!!!
      @@@@@@@@@@     ##                ##   _$$_     _$$_            \\//              +++++++++++         !!!!!!!!!!!
        
    
    \nDeveloper: Dev. Gautam Kumar
    """"")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:  
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        query = input("You're not clear please type it!")
        return query
    return query
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Jarvis welcomes you Gautam Sir!, here are some headlines for you")
    speak("Should I read headlines for you?")
    read_news_ask = takeCommand()
    if read_news_ask == "yes":
        read_news()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('useronelaptop001@gmail.com', "$_SERVER['REQUEST_METHOD']")
    server.sendmail('useronelaptop001@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    print_logo()
    wishMe()
    run_u = True
    while run_u == True:
    
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:            
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        # To play on YouTube
        elif 'play' in query:
            respond = query.replace("play","playing")
            speak(respond)
            pywhatkit.playonyt(query)
        #To open Youtube 
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.get(chrome_path).open("https://youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.get(chrome_path).open("google.com")

        elif 'open stackoverflow' in query:
            speak("opening stackopverflow")
            webbrowser.get(chrome_path).open("stackoverflow.com")
        elif 'start songs' in query:
            speak("starting songs")
            music_dir = 'E:\\dev_n\\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[random.randrange(0,10)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\Anil%20Kurmi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'search user' in query:
            responde = query.replace("search","searching")
            speak(responde)
            user_name = query.replace(query,"search user")
            spy_scrapper(user_name)
        
        elif  query=='nothing dear':
             run_u = False
        elif query in resp: 
            speak(random.choice(resp[query]))
        
            
