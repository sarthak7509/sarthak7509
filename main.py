from kivymd.app import MDApp
import requests
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import asyncio


class MainScreen(Screen):
    cov = ObjectProperty(None)
    lab= ObjectProperty(None)
    tab = ObjectProperty(None)
    fab = ObjectProperty(None)
    def m(self):
        url = 'https://api.rootnet.in/covid19-in/stats/latest'
        code = self.cov.text
        json_data = requests.get(url).json()
        s = json_data['data']['regional'][int(code)]['loc']
        d = json_data['data']['regional'][int(code)]['deaths']
        c = json_data['data']['regional'][int(code)]['totalConfirmed']
        self.lab.text = "State: " + s
        self.tab.text = "Deaths: "+str(d)
        self.fab.text = "Confirmed: "+str(c)


class MainApp(MDApp):
    def build(self):
        return MainScreen()

MainApp().run()