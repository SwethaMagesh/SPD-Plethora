from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivymd.theming import ThemeManager
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import re
from kivy.uix.floatlayout import FloatLayout
import pyperclip

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
        try:
            
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
        except:
            pop=Popup(title='Some error occurred',content=Label(text='Try again',color=(1,1,1,1)),size_hint=(None,None),size=(350,100))
            pop.open()
            
