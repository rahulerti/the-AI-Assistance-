# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 10:08:15 2023

@author: Rahul Debnath
"""
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
#Initialize TTS engine using Windows speech API (SAPI5)
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)#Queue the text to be spoken
    engine.runAndWait() # run the seech engine


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your ai assistant. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user 

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    r.adjust_for_ambient_noise(source, duration=1)  # Calibrate to background noise

    r.energy_threshold = 300       # Minimum energy to consider audio as speech
    r.pause_threshold = 1          # Seconds of silence before stopping recording

    audio = r.listen(source)       # Capture the audio

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        speak("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bwubts20104@brainwareuniversity.ac.in', 'password')
    server.sendmail('bwubts20104@brainwareuniversity.ac.in', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'search' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("youtube open")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("google open")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("stackflow is open")


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'sent mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rahuldebnath39821@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")    

