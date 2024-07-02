from kivymd.app import MDApp
from kivymd.toast import toast

class MyApp(MDApp):
    def build(self):
        # Example usage of toast notification
        toast("Hello, World!")

MyApp().run()
