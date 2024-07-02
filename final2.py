from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp



class MyApp(MDApp):
    def build(self):

        bldr = Builder.load_file("admin_dashboard.kv")

        return bldr




if __name__ == "__main__":
    MyApp().run()
