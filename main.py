import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


class MainScreen(Screen):
    weight = ObjectProperty(int)
    hei = ObjectProperty(int)
    def btn(self):
        s = self.weight.text
        n = self.hei.text
        if s == "" and n == "":
            Pop_up()
        else:
            b = ((int(s) / (int(n) * int(n))) * 10000)
            print(b)
            if b == 0:
                show_pop()
            elif b <= 18.5:
                sm.current = "third"
            elif b < 24.9 :
                sm.current = "fourth"
            elif b > 24.9:
                sm.current = "five"


class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    def btn2(self):
        sm.current = "First"

class FourthScreen(Screen):
    wimg = Image(source = 'land.png')


class FifthScreen(Screen):
    pass

class Manager(ScreenManager):
    pass

class P(FloatLayout):
    pass
class C(FloatLayout):
    pass


kv = Builder.load_file("my.kv")

sm = Manager()

screens = [MainScreen(name="First"), ThirdScreen(name="third"), SecondScreen(name="second"), FourthScreen(name="fourth"), FifthScreen(name="five")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "First"


class MyApp(App):
    def build(self):
        return sm

def Pop_up():
    show = P()
    popupwindow = Popup(title="ALERT!!!", content=show, size_hint=(None,None),size=(400,400))

    popupwindow.open()

def show_pop():
    dis = C()
    showwindow = Popup(title="Alert!!!", content=dis, size_hint=(None,None),size=(400,400))
    showwindow.open()


if __name__ == "__main__":
    MyApp().run()