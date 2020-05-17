import speech_recognition as sr
import pyttsx3
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class SpeechLayout(Widget):
    def change(self):
        if self.ids.choice.text=='Text to Speech':
            self.ids.sm.current='first'
        else:
            self.ids.sm.current='second'
        
    def speakOut(self):
        try:
            text=self.ids.tToS.text
            engine = pyttsx3.init()
            engine.say(text)
            engine.setProperty('rate',120)
            engine.setProperty('volume', 0.9)
            engine.runAndWait()
        except:
            pop=Popup(title='Some error occurred',content=Label(text='Try again',color=(1,1,1,1)),size_hint=(None,None),size=(350,100))
            pop.open()
    
    def recog(self):
        
        r=sr.Recognizer()
        with sr.Microphone() as source:            
            audio = r.listen(source)
            try:
                text=r.recognize_google(audio)
                self.ids.result.text=text
            except :
                self.ids.result.text="Sorry Voice Not recognisable"
        
        
