from kivymd.app import MDApp
from kivy.uix.widget import Widget
import os
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import tkinter

from kivy.properties import ObjectProperty,StringProperty
from PIL import Image,ImageOps
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivymd.toast import toast
from kivy.uix.gridlayout import GridLayout



class ImageLayout1(Widget):
    im1=ObjectProperty(None)
    im2=ObjectProperty(None)
    global filename
    filename="1.jpg"
    def SaveFile(self):  
        toast('Saved successfully in gallery as out.jpg')
        
        
            

    def tint(self):
        try:
            
            if os.path.exists("out.jpg"):
                os.remove("out.jpg")
            img=Image.open(self.filename)
            imgG=img.convert("L")
            img1=ImageOps.colorize(imgG,black=self.ids.spin.text,white="white")
            img2=img1.save('out.jpg')
        
        except:
            pop=Popup(title='Some error occurred',content=Label(text='Try again'),size_hint=(None,None),size=(350,100))
            pop.open()
           
        



    def grey(self):
        try:
            
            if os.path.exists("out.jpg"):
                os.remove("out.jpg")
            img=Image.open(self.filename)
            imgG=img.convert("L")
            img2=imgG.save('out.jpg')
           
        except:
            pop=Popup(title='Some error occurred',content=Label(text='Try again'),size_hint=(None,None),size=(350,100))
            pop.open()
            
        
    def flip(self,dir):
        try:
            
            if os.path.exists("out.jpg"):
                os.remove("out.jpg")
            img=Image.open(self.filename)
            img=img.convert('RGB')
            if dir=='v' :
                img1=ImageOps.flip(img)
            elif dir=='h':
                img1=ImageOps.mirror(img)
            elif dir=='neg':
                img1=ImageOps.invert(img)
            img2=img1.save('out.jpg')
            
           

        except:
            pop=Popup(title='Some error occurred',content=Label(text='Try again'),size_hint=(None,None),size=(350,100))
            pop.open()
            
            
    def Convert(self):
        try:
            
            self.im2.source='old.jpg'
            for i in range(0,5):
                pass
            self.im2.source='out.jpg'
        except:
            pop=Popup(title='Some error occurred',content=Label(text='Try again'),size_hint=(None,None),size=(350,100))
            pop.open()
            
    def workOn(self):
        try:
            
            image=Image.open('out.jpg')
            image.save('workagain.jpg')
            self.filename='workagain.jpg'
            self.im1.source='old.jpg'
            print('test')
            self.im1.source=self.filename
        except:
            pop=Popup(title='Some error occurred',content=Label(text='Try again'),size_hint=(None,None),size=(350,100))
            pop.open()
            
        
    def browse(self):
        try:
            
            global filename
            from tkinter import ttk
            from tkinter import filedialog           
            self.filename= filedialog.askopenfilename(initialdir="/",title="Select A file",filetype=(("jpeg files","*.jpg"),("all files","*.*")))
            self.im1.source=self.filename
        except:
            pop=Popup(title='Some error occurred',content=Label(text='Try again'),size_hint=(None,None),size=(350,100))
            pop.open()
            

    def resetSlider(self):
        self.ids.slid1.value=1

    def rot90(self):
        try:
            
            if os.path.exists("out.jpg"):
                os.remove("out.jpg")
            img=Image.open(self.filename)
            imgG=img.rotate(90)
            for i in range(0,5):
                pass
            img2=imgG.save('out.jpg')

        except:
            pop=Popup(title='Some error occurred',content=Label(text='Try again'),size_hint=(None,None),size=(350,100))
            pop.open()
            

    def crop(self):
        try:
            
            if os.path.exists("out.jpg"):
                os.remove("out.jpg")
            img=Image.open(self.filename)
            SZ=img.size
            l=SZ[0]*self.ids.left.value
            r=SZ[0]*self.ids.rgt.value
            t=SZ[1]*self.ids.top.value
            b=SZ[1]*self.ids.btm.value
            box=(l,t,r,b)
            if l>r or t>b:
                pop=Popup(title='Some error occurred',content=Label(text='Try again'),size_hint=(None,None),size=(350,100))
                pop.open()
                
            else:
                img1=img.crop(box)
                img1.save('out.jpg')
        except:
            pop=Popup(title='Some error occurred',content=Label(text='Try again'),size_hint=(None,None),size=(350,100))
            pop.open()
    

