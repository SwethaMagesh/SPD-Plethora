import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print('Speak Anyhting')
    audio = r.listen(source)

    try:
        text=r.recognize_google(audio)
        print('you say :{}',format(text))
    except :
        print('Sorry could nt recognize ur voice')
