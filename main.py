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
            self.weight.text = ""
            self.hei.text = ""
        else:
            b = ((int(s) / (int(n) * int(n))) * 10000)
            print(b)
            if b == 0:
                show_pop()
                self.weight.text = ""
                self.hei.text = ""
            elif b <= 18.5:
                sm.current = "third"
                self.weight.text = ""
                self.hei.text = ""
            elif b < 24.9 :
                sm.current = "fourth"
                self.weight.text = ""
                self.hei.text = ""
            elif b > 24.9:
                sm.current = "five"
                self.weight.text = ""
                self.hei.text = ""


class SecondScreen(Screen):
    def btn5(self):
        sm.current = "six"


class ThirdScreen(Screen):
    def btn2(self):
        sm.current = "First"

class FourthScreen(Screen):
    def btn3(self):
        sm.current = "First"
class FifthScreen(Screen):
    def btn4(self):
        sm.current = "First"

class SixScreen(Screen):
    que = ObjectProperty(None)
    ans = ObjectProperty(None)
    def btn6(self):
        sm.current = "second"
    def answere(self):
        ques = self.que.text
        self.ans.text = ""
        if ques == "hi":
            self.ans.text = "Hello dear how may I help you!"
        elif ques == "how does this app works":
            self.ans.text = "This app works on the basis of \n BMI by taking your Height and Weight"
        elif ques == "customer service":
            self.ans.text = "Email: bhatnagarsarthak3@gmail.com\nMobile number: 8969671739"
        elif ques == "Terms and conditions":
            self.ans.text = "This app is not for:\n1)BodyBuilder\n2)Pregnant lady\n"
        else:
            self.ans.text = "Invalid Question"
        self.que.text = ""


class Manager(ScreenManager):
    pass

class P(FloatLayout):
    pass
class C(FloatLayout):
    pass


kv = Builder.load_file("my.kv")

sm = Manager()

screens = [MainScreen(name="First"), ThirdScreen(name="third"), SecondScreen(name="second"), FourthScreen(name="fourth"), FifthScreen(name="five"), SixScreen(name="six")]
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