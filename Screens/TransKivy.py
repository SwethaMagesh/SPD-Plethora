from kivymd.app import MDApp
from googletrans import Translator
import googletrans
import pyperclip
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget
from kivymd.theming import ThemeManager


def get_key(val): 
    for key, value in googletrans.LANGUAGES.items(): 
         if val.lower() == value.lower():
             print(key)
             return key 
  
    return "error"


class TransLayout(Widget):
    
    pass
    def copyClip(self):
        #Clipboard.copy(self.ids.res.tcext)
        pyperclip.copy(self.ids.dest.text)
    def translate(self):
        print('function works')
        translator=Translator()
        S=get_key(self.ids.spin2.text)
        if S=='error':
            S='en'
            self.ids.spin2.text='English'
        D=get_key(self.ids.spin1.text)
        if D=='error':
            D='fr'
            self.ids.spin1.text='French'
        res=translator.translate(self.ids.src.text,src=S,dest=D)
        self.ids.dest.text=res.text
        print(res.text)

    def detect(self):
        print('the fun works')
        tr=Translator()
        detected=tr.detect(self.ids.src.text)
        L=googletrans.LANGUAGES.get(detected.lang).upper()
        labeltext='The language detected is '+L+'\n The accuracy of detection is '+str(detected.confidence*100)
        print(labeltext)
        self.ids.detect.text=labeltext
        self.ids.spin2.text=L
        
        
    

##                
##class myTransApp(MDApp):   
##    def build(self):
##        self.theme_cls.primary_palette = "Pink"
##        return TransLayout()
##
##
##myTransApp().run()
