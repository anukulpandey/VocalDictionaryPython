from PyDictionary import PyDictionary as pd
import pyttsx3 as ps
import speech_recognition as sr

# Functions
def listen():
    """
    Listens to whatever the user says and return the same as string
    """
    hear = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening...")
        hear.pause_threshold = 1
        audio = hear.listen(source)
        query = hear.recognize_google(audio, language='en-in')
    return query

def speak(string):
    """
    Speaks the string given as Input
    """
    engine = ps.init()
    engine.setProperty('rate', 175)
    engine.say(string)
    engine.runAndWait()

print("Welcome to Audio Dictionary:start while you are reading!Read the word it will tell you the meaning")
while True:
    while True:
        try:
            print("listening...")
            word=listen()
            print(word)
            break
        except Exception as e:
            print("--------can not find--------")
            print("listening...")

    print(pd.meaning(word))
    speak(pd.meaning(word))