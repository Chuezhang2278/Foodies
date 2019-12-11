import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Please speak")
    audio = r.listen(source)

print(r.recognize_google(audio))
