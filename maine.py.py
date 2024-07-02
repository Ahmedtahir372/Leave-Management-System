from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

Window.size = (310, 570)

""",red,pink, 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 
'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']"""


class LeavesystemApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"
        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("test_appdrawer.kv"))
        sm.add_widget(Builder.load_file("add_employee.kv"))

        return sm


LeavesystemApp().run()
