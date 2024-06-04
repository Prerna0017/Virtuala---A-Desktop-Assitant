import threading
from ScreenRec import screenRecord
import pyttsx3, datetime, speech_recognition as sr

def command():
    """taking user mic input as a command"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold=10000
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        global query 
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")
    except Exception as e:  
        print("Say that again please...") 
        return "None"
    return query

def main():
    stop_threads = False
    screenRecoThread = threading.Thread(target = screenRecord, args = (lambda : stop_threads, ))
    query = command().lower()

    if 'launch' in query:
        screenRecoThread.start()
        print("Started")

    elif 'close' in query:
        try:
            stop_threads = True
            screenRecoThread.join()
            print('thread killed')
            stop_threads = False
        except:
            print("sgr")

while True:
    main()