from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

Window.size = (310, 570)


class Screen_Register(Screen):
    pass


class Screen_Home(Screen):
    pass


class Screen_A(Screen):
    pass


class Screen_B(Screen):
    pass


class Screen_C(Screen):
    pass


class Screen_A1(Screen):
    pass


class Screen_B1(Screen):
    pass


class Screen_C1(Screen):
    pass


class Screen_A2(Screen):
    pass


class Screen_B2(Screen):
    pass


class Screen_C2(Screen):
    pass


""",red,pink, 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen',
'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']"""


class ListBuilderApp(MDApp):
    def build(self):

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"
        bldr = Builder.load_file("fileprj.kv")
        return bldr


ListBuilderApp().run()
