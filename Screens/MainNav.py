from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import NavigationLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class NavigationDrawer(NavigationLayout):
    def back_to_home_screen(self):
        self.ids.navsm.current='home'

class ContentNavigationDrawer(BoxLayout):
    pass




