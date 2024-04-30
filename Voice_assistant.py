import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime 
import wikipedia


# Function to take command from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return Query

# Function to speak
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio) 
    engine.runAndWait()

# Function to tell the day
def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

# Function to tell the time
def tellTime():
    time = datetime.datetime.now().strftime("%H:%M")
    print(time)
    speak("The time is " + time)

# Function to greet the user
def Hello():
    speak("hello sir I am your desktop assistant. Tell me how may I help you")

# Function to handle user queries
def Take_query():
    Hello()
    while True:
        query = takeCommand().lower()
        if "open geeks for geeks" in query:
            speak("Opening Geeks for Geeks ")
            webbrowser.open("https://www.geeksforgeeks.org/")
        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("https://www.google.com/")
        elif "which day it is" in query:
            tellDay()
        elif "tell me the time" in query:
            tellTime()
        elif "bye" in query:
            speak("Bye. Check Out GFG for more exciting things")
            break
        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)
        elif "tell me your name" in query:
            speak("I am Jarvis. Your desktop Assistant")

if __name__ == '__main__':
    Take_query()
