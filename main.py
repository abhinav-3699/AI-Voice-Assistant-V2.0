# .............AI Voice Assistant V1.5.............

#New features Added !


# Additional Libraries used --> 
#                - pyttsx3
#                - Speech Recognition
#                - datetime
#                - wikipedia
#                - webbrowser
#                - pywhatkit
#                - pyautogui

# Contact { 
            #instagram : _.abh.i_.x
            #gmail : abhinavsanthosh3699@gmail.com

# ! The Code Is In Initional Stage .....
                # Future updates Soon >> :)import pyttsx3import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import webbrowser
import pyautogui

import speech_recognition as sr
import os
import time
import datetime
from playsound import playsound
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Recognizing...")
        queri = r.recognize_google(audio,language='en-in')
        print(f"You Said : {queri}")

    except Exception as e:
        return "None"

    return queri

current_time = datetime.datetime.now()
hour= current_time.hour
min = current_time.minute
final_time = (hour, min)
def greet_me():
    if hour>=0 and hour<12 :
        speak(f"Good morning sir, its {final_time}A,M, how can i assist you")
    elif hour>=12 and hour<16:
        speak(f"Good afternnon sir, its {final_time}P,M, how can i assist you")

    elif hour>=16 and hour<18:
        speak(f"Good evening sir, its {final_time}P,M, how can i assist you")

    else :
        speak(f"Welcome back sir, its {final_time}P,M, how can i assist you")
    
    return

def googlesearch(query):
    query = query.replace("google","")
    speak("This is what i found on google")

    try:
        pywhatkit.search(query)
        result = wikipedia.summary(query,1)
        speak(result)

    except:
        speak("No sepakable output found")



def simple_alarm_clock():
    speak("Enter the time for the alarm in the following format")
   
    alarm_time = input("Enter the time for the alarm in HH:MM format (24-hour): ")
    
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        if alarm_hour < 0 or alarm_hour > 23 or alarm_minute < 0 or alarm_minute > 59:
            raise ValueError
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM format (24-hour).")
        return
    
    print(f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}.")
    
    while True:
        # Get the current time
        current_time = datetime.datetime.now()
        current_hour = current_time.hour
        current_minute = current_time.minute
        
       
        remaining_minutes = ((alarm_hour - current_hour) * 60 + alarm_minute - current_minute) % (24 * 60)
        
        if remaining_minutes == 0:
            # Time to trigger the alarm
            print("Alarm triggered! Time to wake up!")
            playsound("music.mp3") 
            break
        else:
          
            hours_left = remaining_minutes // 60
            minutes_left = remaining_minutes % 60
            print(f"Time remaining: {hours_left} hours {minutes_left} minutes.")
            time.sleep(60) 






    







    

if __name__ == "__main__":
    greet_me()
    while True:
        query = command().lower()
        if "hello" in query:
            speak("Hi sir, how are you")

        elif "how are you" in query:
            speak("I am fine sir, how are you")

        elif "i am fine" in query:
            speak("great, glad to hear that")

        elif "what's the time now" in query:
            if hour>=0 and hour<12:
                speak(f"its {final_time}A,M")

            else :
                speak(f"Its {final_time}P,M")

        elif "who are you" in query:
            speak("I am an a,i machine develped in python programming language")

        elif "google" in query:
            googlesearch(query)

        elif "open new tab" in query:
            pyautogui.hotkey("ctrl","t")

        elif "close it" in query:
            pyautogui.hotkey("ctrl","w")

        elif "set alarm" in query:
            
            simple_alarm_clock()







        


        elif "go to sleep" in query:
            speak("I hope it helped ")
            break


        elif "exit" in query:
            speak("I hope it helped ")
            break