
from tkinter import *
from tkinter import filedialog,mainloop
from tkinter.ttk import *
from PIL import ImageTk, Image
import pytesseract

def filebrowse():
    filename=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print(filename)


def ImageProcess():
    newIm=Image.open('colorText.jpg')
    newIm=newIm.resize((750,300))
    newImDis=ImageTk.PhotoImage(newIm)
    ImRes.configure(image=newImDis)
    ImRes.image=newImDis

def TextProcess():
    Textwindow=Toplevel(root)
    Textwindow.title("TEXT")
    Textwindow.geometry("700x500+400+200")
    Ques=Text(Textwindow,height=10,bg='#f5e1d0')
    Ques.place(x=30,y=10)
    Ans=Text(Textwindow,height=10,bg='#fbe1fc')
    Ans.insert(INSERT,"The ans goes here")
    Ans.place(x=30,y=250)
    
    textFn=Combobox(Textwindow)
    textFn['values']=("Translate","Keywords list","Blah blah")
    textFn.place(x=100,y=200)

    fetch=Button(Textwindow,text="Fetch result")
    fetch.place(x=300,y=200)
    mainloop()
    
root = Tk()
root.title("SPD")
root.geometry("800x700")

img=Image.open('text1.jpg')
img=img.resize((750,300))
imgDis=ImageTk.PhotoImage(img)


ImageLabel=Label(root,image=imgDis)
ImRes=Label(root)
button=Button(root,text='Fetch processed',command=ImageProcess)
#bg='#d8ace8'
CBox=Combobox(root)
CBox['values']=('Black and White','Mirror Image','Sharpen','Contrast')
TextBox=Button(root,text='Fetch text',command=TextProcess)
Browse=Button(root,text="Select a pic",command=filebrowse)
L1=Label(root,text="Image 1")
L2=Label(root,text="Resultant Image")

#Placements
ImageLabel.place(x=25,y=0)
ImRes.place(x=25,y=350)
button.place(x=450,y=315)
CBox.place(x=300,y=315)
TextBox.place(x=550,y=315)
Browse.place(x=200,y=315)
L1.place(x=450,y=0)
L2.place(x=450,y=350)

mainloop()





