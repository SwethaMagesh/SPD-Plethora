from kivymd.app import MDApp
import pytesseract
from pytesseract import image_to_string
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pyttsx3
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.label import Label
global root
global flag
flag=0
def createTkinter():
    global root
    root=tk.Tk()
    root.title('Browsing a file')
    root.tk.call('wm','iconphoto',root._w,tk.PhotoImage(file='icon.png'))
    root.geometry("400x100+300+300")
    w=tk.Label(root,text="You will be prompted to choose any pictures from your \n device's storage.Click OK to continue",font="Helvetica 18 bold")
    w.grid(row=0,column=0)
    w.configure(font=("Courier", 8, "bold"))
    w=Button(root,text='Ok',fg='#e75480',borderwidth=4,width=15,command=lambda:open_file())
    w.grid(row=3,column=0)
    w=Button(root,text='Cancel',fg='#e75480',borderwidth=4,width=15,command=lambda:Close_file())
    w.grid(row=6,column=0)

def Close_file():
    global root
    global flag
    root.destroy()
    flag=0

def open_file():
    global flag
    global root
    global filename    
    filename= filedialog.askopenfilename(initialdir="/",title="Select A file",filetype=(("jpeg files","*.jpg"),("all files","*.*")))
    if filename=="":
        flag=0
    else:
        flag=1
    root.destroy()
    
    
    
class ImageToText(Widget):
    global text
    text=" "
    global filename
    filename=" "
    def TextConversion(self):
        from PIL import Image
        global text
        pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        try:
            image = Image.open(filename)
            text = pytesseract.image_to_string(image)
            text=text.replace('\n',' ')
            self.textLbl.text=text
        except:
            pop=Popup(title='Some error occurred',content=Label(text='Try again'),size_hint=(None,None),size=(350,100))
            pop.open()
            
    def SpeechConversion(self):
        if text==" ":
            pop=Popup(title='Some error occurred',content=Label(text='Try again',color=(1,1,1,1)),size_hint=(None,None),size=(350,100))
            pop.open()
        else:
            engine = pyttsx3.init()
            engine.say(text)
            engine.setProperty('rate',120)
            engine.setProperty('volume', 0.9)
            engine.runAndWait()
    def BrowseImage(self):
        global filename
        global flag
        createTkinter()
        tk.mainloop()
        #filename= filedialog.askopenfilename(initialdir="/",title="Select A file",filetype=(("jpeg files","*.jpg"),("all files","*.*")))
        #self.label.configure(text=self.filename)
        if flag==1:
            self.label_wid1.source=filename
    
