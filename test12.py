from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import ScreenManager
class LeaveApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette = "Cyan"
        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("new_signup2.kv"))
        sm.add_widget(Builder.load_file("employee_details.kv"))

        return sm

    def on_start(self):
        for i in range(20):
            items = OneLineListItem(text='Item' + str(i))
            self.root.get_screen("scr").ids.container.add_widget(items)
LeaveApp().run()
