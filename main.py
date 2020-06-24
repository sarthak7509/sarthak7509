from kivymd.app import MDApp
import requests
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager,FallOutTransition,SwapTransition
from kivy.properties import ObjectProperty
from kivymd.theming import ThemeManager



class MainScreen(Screen,MDApp):
    cov = ObjectProperty(None)
    lab= ObjectProperty(None)
    tab = ObjectProperty(None)
    fab = ObjectProperty(None)
    nab = ObjectProperty(None)
    def __init__(self, **kwargs):
        try:
            super(MainScreen, self).__init__(**kwargs)
            url = 'https://api.rootnet.in/covid19-in/stats/latest'
            json_data = requests.get(url).json()
            t = json_data['data']['summary']['total']
            dea = json_data['data']['summary']['deaths']
            reco = json_data['data']['summary']['discharged']
            self.lab.text = "INDIA"
            self.tab.text = "Confirmed: " + str(t)
            self.fab.text = "Deaths: " + str(dea)
            self.nab.text = "Recovered: " + str(reco)
        except requests.exceptions.ConnectionError:
            self.lab.text = "Connection error"
            self.fab.text = "Check your internet\nconnection"
    def m(self):
        self.lab.text = ""
        self.tab.text = ""
        self.fab.text = ""
        self.nab.text = ""
        try:
            url = 'https://api.rootnet.in/covid19-in/stats/latest'
            code = self.cov.text
            json_data = requests.get(url).json()
            if code == "" or code =="India" or code == "india":
                t = json_data['data']['summary']['total']
                dea = json_data['data']['summary']['deaths']
                reco = json_data['data']['summary']['discharged']
                self.lab.text = "INDIA"
                self.tab.text = "Confirmed: " + str(t)
                self.fab.text = "Deaths: " + str(dea)
                self.nab.text = "Recovered: " + str(reco)

            else:
                s = json_data['data']['regional'][int(code)]['loc']
                d = json_data['data']['regional'][int(code)]['deaths']
                c = json_data['data']['regional'][int(code)]['totalConfirmed']
                r = json_data['data']['regional'][int(code)]['discharged']
                self.lab.text = "State: " + s
                self.tab.text = "Deaths: "+str(d)
                self.fab.text = "Confirmed: "+str(c)
                self.nab.text = "Recovered: "+str(r)
        except requests.exceptions.ConnectionError:
            self.lab.text = "Connection error"
            self.fab.text = "Check your internet\nconnection"
        except ValueError:
            self.lab.text = "Enter State\n number"
            self.nab.text = "Click on menu Button\nto Know Your\nState Number"
        except IndexError:
            self.lab.text = "Please Enter Valid State number"
            self.fab.text = "Click on menu Button\nto Know Your\nState Number"

    def btn(self):
        sm.current = "s"
    
class SecondScreen(Screen,MDApp):
    def btn(self):
        sm.current="f"

class Manager(ScreenManager):
    pass

kv = Builder.load_file("main.kv")
sm=Manager(transition=SwapTransition())
screens = [MainScreen(name="f"),SecondScreen(name="s")]
for screen in screens:
    sm.add_widget(screen)
sm.current = "f"

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.primary_hue = '800'
        return sm

MainApp().run()