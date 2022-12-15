import datetime
import smtplib
import webbrowser as wb
import os
import pyautogui # pip install pyautogui
import psutil # pip install psutil
import pyjokes # pip install pyjokes
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia  # pip install wikipedia

engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate=150
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("The date today is ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir! ")
    hour=datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    elif hour>=18 and hour<24:
        speak("Good evening")
    else:
        speak("Good night")

    speak("Gawd at your service. How can I help you? ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        
        return "None"

    return query

def screenshot():
    img=pyautogui.screenshot()
    img.save("C:\\Users\\91888\\Pictures\\ss.png")

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at " + usage)

    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    speak("percent")

def jokes():
    speak(pyjokes.get_joke())

if __name__=="__main__":
    wishme()

    while True:
        query=takeCommand().lower()
        print(query)

        if "how are you" in query:
            speak("I am doing great Sir. Thanks for asking")
        elif "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("Goodbye Sir")
            quit()
        elif "wikipedia" in query:
            speak("Searching on Wikipedia...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak(result)
        elif "Log out" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1") 

        elif "play song" in query:
            songs_dir=("C:\\Users\\91888\\Music")
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif "remember that" in query:
            speak("What should I remember")
            data=takeCommand()
            speak("You told me to remember that" + data)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()

        elif "remind me" in query:
            remember=open("data.txt","r")
            speak("You told me to remember that" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Screenshot taken successfully")

        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes() 