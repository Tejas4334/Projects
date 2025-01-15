import speech_recognition as sr # importing Speech recognition library

recognizer = sr.Recognizer() # using Recognizer method
with sr.Microphone() as source: #using microphone as source
    print("Please say something...")
    audio_data = recognizer.listen(source) # storing all mic data at a address (here named as audio_data)
    # print(str(audio_data))
    print("Recognizing...")
    try:
        text = recognizer.recognize_google(audio_data) # using  google's recognizer to convert audio_data into text
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Could not understand audio")
        # print("You said: " + text)
    except sr.RequestError as e:
        print(f"Request error; {e}")
