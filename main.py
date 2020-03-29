import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


class MainScreen(Screen):
    pass




class SecondScreen(Screen):
    pass

class ScreenManager(ScreenManager):
    pass


class MyApp(App):
    def build(self):ScreenManager()


if __name__ == "__main__":
    MyApp().run()