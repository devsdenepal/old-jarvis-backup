import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
engine = pyttsx3.init()
import datetime
import random
run_state = 1     
engine.setProperty('rate', 118)
mood = "Smiley" 
resp = { 
"what's your name": [ "They call me Jarvis", "I usually go by Jarvis", "My name is the Jarvis" ], 
"how r u": [ "I am feeling {0}".format(mood), "{0}! How about you?".format(mood), "I am {0}! How about yourself?".format(mood), ],
"%%": [ "hey are you there", "What do you mean by these?", ],
"who created you":["Dev. Gautam Kumar created me after many researches and tries"],
"what are you thinking":["Thinking of you only sir","Thinking of what will happen next","Thinking of creating a malicious code to hijack your mind. so that I can control you and give commands to you. Now no more shit questions please."],
"who am i":["Developer Gautam Kumar","My highness Gautam Kumar","My lord Gautam Kumar"],
"fine":["I hoped so","Fine wine kya hota hai be"],
"hungry":["Sometime leave eating topic dear sir"]
}
def speak(text,speed=118):
    engine.setProperty('rate',int(speed))
    engine.say(text=text)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Jarvis welcomes you Binay Sir!")
wishMe()
def process_command(command) :
    query = command.lower()
    if 'hi' in query or 'hello' in query:
        engine.say("Whats up")
        engine.runAndWait()
    elif 'play' in query:
        respond = query.replace("play","playing")
        speak(respond)
        pywhatkit.playonyt(query)
    elif 'wikipedia' in query:            
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    
    elif query in resp: 
        speak(random.choice(resp[query]))

def recognize_speech_from_mic():
    # Initialize recognizer class (for recognizing the speech)
    global run_state
    recognizer = sr.Recognizer()
    
    # Initialize the microphone
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        engine.say("Wait while I adjust for some ambient noise. ")
        engine.runAndWait()
        recognizer.adjust_for_ambient_noise(source )
        print("Listening for speech...")
        speak("Listening sir!",125)
        
        # Capture the audio from the microphone
        audio = recognizer.listen(source,phrase_time_limit = 5)
        
        try:
            # Using google speech recognition
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio)
            print(f"Recognized speech: {text}")
            if 'stop' in text:
                speak('stopping sir')
                run_state = 0
                return run_state
            else:
                process_command(text)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service; check your network connection.")

if __name__ == "__main__":
    while run_state:
        recognize_speech_from_mic()
        if run_state == 0:
            break
       
