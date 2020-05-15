import speech_recognition as sr
import pyttsx3
from kivy.uix.widget import Widget


class SpeechLayout(Widget):
    def change(self):
        if self.ids.choice.text=='Text to Speech':
            self.ids.sm.current='first'
        else:
            self.ids.sm.current='second'
        
    def speakOut(self):
        text=self.ids.tToS.text
        engine = pyttsx3.init()
        engine.say(text)
        engine.setProperty('rate',120)
        engine.setProperty('volume', 0.9)
        engine.runAndWait()
    
    def recog(self):
        
        r=sr.Recognizer()
        with sr.Microphone() as source:
            
            audio = r.listen(source)
            try:
                text=r.recognize_google(audio)
                self.ids.result.text=text
                #print('you say :'+format(text))
            except :
                #print('Sorry Cannot recognize your voice')
                self.ids.result.text="Sorry Voice Not recognisable"
        
        
