from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.theming import ThemeManager
from database import DataBase
from kivy.config import Config
from kivy.core.window import Window
#Window.size = (400, 400)
Config.set('graphics','resizable',0)
Builder.load_file('Main.kv')
import MainNav
Builder.load_file("mytrans.kv")
Builder.load_file("myTextToText.kv")
Builder.load_file("imageEdit.kv")
Builder.load_file("imageText.kv")
Builder.load_file("speech.kv")
Builder.load_file("Homepage.kv")
import TransKivy
import textToText
import ImageEdit
import ImageText
import audio1
import Homepage
db = DataBase("users.txt")
class WindowManager(ScreenManager):
    pass

class NavScreen(Screen):
    def on_pre_enter(self):
        Window.size = (800, 600)
    pass
class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def on_pre_enter(self):
        Window.size = (400, 400)
    pass

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password.text != "":
                db.add_user(self.email.text.strip(), self.password.text.strip(), self.namee.text.strip())
                self.reset()
                self.manager.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        self.manager.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def on_pre_enter(self):
        Window.size = (400, 400)
    pass

    def loginButton(self):
        if db.validate(self.email.text.strip(), self.password.text.strip()):
            #MainWindow.current = self.email.text
            self.reset()
            self.manager.current = "main"
        else:
            invalidLogin()

    def createButton(self):
        self.reset()
        self.manager.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

##
##class MainWindow(Screen):
##
##    def logOut(self):
##        self.manager.current = "login"
##
##    def on_enter(self, *args):
##        self.manager.current="main"





def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(250, 100))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(350, 100))

    pop.open()

    


##sm = WindowManager()
##screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),NavScreen(name="main")]
##for screen in screens:
##    sm.add_widget(screen)
##self.manager.current = "login"


class LoginApp(MDApp):
    
    def __init__(self, **kwargs):        
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Pink"
        self.title="Plethora"
    
    def build(self):
        
        kv = Builder.load_file("Loginlayout.kv")
        return kv


if __name__ == "__main__":
    LoginApp().run()
