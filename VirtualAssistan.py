# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 07:41:55 2022

@author: ASUS
"""

#SPEECH RECOGNITION
import speech_recognition as sr
import os
import re
import webbrowser
import datetime

def greet():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        print("Selamat Pagi")
    if currentH >= 12 and currentH < 18:
        print("Selamat Siang")
    if currentH >= 18 and currentH < 0:
        print("Selamat Malam")
        
greet()

def myCommand():
    "listens for commands"
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Siap....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
    try:
        command = r.recognize_google(audio).lower()
        print('Hilmy : ' + command + '\n')
        
    except sr.UnknownValueError:
        print('Hilmy: Tidak bisa didengar')
        command = myCommand();
        
    return command

def assistant(command):
    "if statement for executing commands"
    
    if 'hello' in command:
        print('Bejo: Hello Hilmy, Apa yang bisa aku bantu?')
    elif 'open google' in command:
        reg_ex = re.search('google (.*)', command)
        url = 'https://www.google.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
    elif 'where is this' in command:
        reg_ex = re.search('google (.*)', command)
        url = 'https://www.google.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
    elif 'thank you' in command:
          print('Bye!')
          exit()
          
while True:
    assistant(myCommand())
        
    
