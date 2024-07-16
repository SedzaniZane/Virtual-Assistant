# This is a sample Python script.
#For the Virtural Assisatant we need the following from the Terminal window at the bottom

#pip install SpeechRecognition
#pip installPyAudio
#pop install pywhatkit
#pip install gtts

import speech_recognition as sr
import pyaudio
import pywhatkit

def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something...")
        audio = recorder.listen(source)

    text = recorder.recognize_google(audio)
    print(f"You said: {text}")
    return text

text = get_audio()

#For searching and playing a clip on youtube
pywhatkit.playonyt("Kelvin Momo-Sukakude")
pywhatkit.search(text)

#if "Youtube" in text.lower():
    #pywhatkit.playonyt(text)
#else:
   # pywhatkit.search(text)
