import speech_recognition as sr


# Initialize the recognizer
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)
result = r.recognize_google(audio)
print(result)