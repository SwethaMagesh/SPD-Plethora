from kivymd.app import MDApp
from kivy.uix.widget import Widget
import os
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import tkinter
#from tkinter import *
from kivy.properties import ObjectProperty,StringProperty
from PIL import Image,ImageOps
class ImageLayout1(Widget):
    im1=ObjectProperty(None)
    im2=ObjectProperty(None)
    global filename
    filename="1.jpg"

    def tint(self):
        if os.path.exists("out.jpg"):
            os.remove("out.jpg")
        img=Image.open(self.filename)
        imgG=img.convert("L")
        img1=ImageOps.colorize(imgG,black=self.ids.spin.text,white="white")
        img2=img1.save('out.jpg')
        #self.im2.source='out.jpg'
        



    def grey(self):
        if os.path.exists("out.jpg"):
            os.remove("out.jpg")
        img=Image.open(self.filename)
        imgG=img.convert("L")
        img2=imgG.save('out.jpg')
        #self.im2.source='out.jpg'
        
    def flip(self,dir):
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
        
        #self.im2.source='out.jpg'       
    def Convert(self):
        self.im2.source='old.jpg'
        for i in range(0,5):
            pass
        self.im2.source='out.jpg'
    def workOn(self):
        image=Image.open('out.jpg')
        image.save('workagain.jpg')
        self.filename='workagain.jpg'
        self.im1.source='old.jpg'
        print('test')
        self.im1.source=self.filename
        
    def browse(self):
        global filename
        from tkinter import ttk
        from tkinter import filedialog           
        self.filename= filedialog.askopenfilename(initialdir="/",title="Select A file",filetype=(("jpeg files","*.jpg"),("all files","*.*")))
        self.im1.source=self.filename

    def resetSlider(self):
        self.ids.slid1.value=1

    def rot90(self):
        if os.path.exists("out.jpg"):
            os.remove("out.jpg")
        img=Image.open(self.filename)
        imgG=img.rotate(90)
        for i in range(0,5):
            pass
        img2=imgG.save('out.jpg')

    def crop(self):
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
            Popup(title="Crop size exceeded",content=Label(text="Alter the crop co-ordinates"),size=(200,200))
        else:
            img1=img.crop(box)
            img1.save('out.jpg')
        
        
##class imageEditApp(MDApp):
##    
##    def build(self):
##        self.theme_cls.primary_palette = "Pink"
##        return ImageLayout1()
##    
##imageEditApp().run()
