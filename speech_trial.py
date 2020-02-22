import analyze as az
#import speech_trial as stt
from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
'''import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()'''


def myCommand():
   

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')


    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand()

    return command

    


def get_text():
    text = myCommand()
    SUBSCRIPTION_KEY_ENV_NAME = "e0a4ec68847644849409dce0a433d785"

   # text =  stt.rec()
    #text = 'can someone pass the dissection sissors?'
    print(text)

    keys = az.key_phrases(SUBSCRIPTION_KEY_ENV_NAME,text)
    ent = az.entity_extraction(SUBSCRIPTION_KEY_ENV_NAME,text)
    print(keys)

    return [keys,ent]

get_text()