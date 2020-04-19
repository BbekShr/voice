import speech_recognition as sr
import re

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something!")
    audio = recognizer.listen(source)

#print("Google Speech Recognition think you said")
#print(recognizer.recognize_google(audio))

words = recognizer.recognize_google(audio)
matches = re.search("my name is (.*)", words)

if "hello" in words:
    print("Hello to you too")
elif matches:
    print(f"Hey, {matches[1]}")
elif "how are you" in words:
    print("I am well, thanks")
elif "goodbye" in words:
    print("Goodbye to you too")
else:
    print("Huh?")
