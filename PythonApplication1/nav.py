from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.list import OneLineIconListItem
from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import NavigationLayout
from kivymd.icon_definitions import md_icons
import re
from googletrans import Translator
import googletrans
from kivy.uix.widget import Widget
from kivymd.theming import ThemeManager
import pyperclip
def get_key(val): 
    for key, value in googletrans.LANGUAGES.items(): 
         if val.lower() == value.lower():
             print(key)
             return key 
  
    return "error"
class NavigationDrawer(NavigationLayout):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass


class navApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Pink"
    def build(self):         
        return NavigationDrawer()




class TransLayout(Widget):
    
    pass
    def copyClip(self):
        #Clipboard.copy(self.ids.res.tcext)
        pyperclip.copy(self.ids.dest.text)
    def translate(self):
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
        tr=Translator()
        detected=tr.detect(self.ids.src.text)
        L=googletrans.LANGUAGES.get(detected.lang).upper()
        labeltext='The language detected is '+L+'\n The accuracy of detection is '+str(detected.confidence*100)
        print(labeltext)
        self.ids.detect.text=labeltext
        self.ids.spin2.text=L
        
    
class TEXTFormatLayout(Widget):
    def analyser(self):
        s=self.ids.ques.text
        wrdcnt=len(s.split(' '))
        charcnt=len(s)
        charWithoutSpace=len(s.replace(' ',''))
        senct=len(s.split('.'))-1
        res='Char count ='+str(charcnt)+'\nChar count without space ='+str(charWithoutSpace)+'\nWord Count ='+str(wrdcnt)+'\nSentence count ='+str(senct)
        self.ids.res.text=res
                
    def copyClip(self):
        #Clipboard.copy(self.ids.res.tcext)
        pyperclip.copy(self.ids.res.text)
    def CpToQ(self):
        self.ids.ques.text=self.ids.res.text
    def upperCap(self):
        self.ids.res.text=self.ids.ques.text.upper()
    def lowerCap(self):
        self.ids.res.text=self.ids.ques.text.lower()
    def SenCap(self):
        s=self.ids.ques.text
        s='. '.join(x.capitalize() for x in s.split('. '))
        self.ids.res.text=s
    def InitCap(self):
        s=self.ids.ques.text
        self.ids.res.text=s.title()
    def replacer(self):
        s=self.ids.ques.text
        res=''
        find=self.ids.finder.text.strip()
        rep=self.ids.replace.text.strip()
        if self.ids.whole.active:
            if self.ids.case.active:
                #print('both wholewords and ignore case')
                x=s.split( )                
                for i in range(len(x)):
                    if x[i].lower()==find.lower():
                        x[i]=rep
                    print(x[i])
                res=' '.join(x)
                

            else:
                #print('just whole words no ignore case')
                x=s.split( )                
                for i in range(len(x)):
                    if x[i]==find:
                        x[i]=rep
                    #print(x[i])
                res=' '.join(x)
        else:
            if self.ids.case.active:
               # print('just ignore case')
                res=re.sub(find,rep,s,flags=re.IGNORECASE)
            else:
               # print('just normal')
                res=s.replace(find,rep)
        self.ids.res.text=res
        


    
        
navApp().run()
