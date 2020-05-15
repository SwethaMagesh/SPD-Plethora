from kivymd.app import MDApp
import pytesseract
from pytesseract import image_to_string
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pyttsx3
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
class SimplePopup(Popup):
    pass
class ImageToText(Widget):
    global text
    text=" "
    global filaname
    filename=" "
    def TextConversion(self):
        from PIL import Image
        global text
        pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        image = Image.open(filename)
        text = pytesseract.image_to_string(image)
        text=text.replace('\n',' ')
        self.textLbl.text=text
    def SpeechConversion(self):
        if text==" ":
            self.fire_popup()
        else:
            engine = pyttsx3.init()
            engine.say(text)
            engine.setProperty('rate',120)
            engine.setProperty('volume', 0.9)
            engine.runAndWait()
    def BrowseImage(self):
        global filename
        filename= filedialog.askopenfilename(initialdir="/",title="Select A file",filetype=(("jpeg files","*.jpg"),("all files","*.*")))
        #self.label.configure(text=self.filename)
        self.label_wid1.source=filename
    def fire_popup(self):
        pops=SimplePopup()
        pops.open()
