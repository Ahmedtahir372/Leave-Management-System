from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
import mysql.connector]




Window.size = (310,570)


""",red,pink, 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 
'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']"""

class LeavesystemApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette = "Cyan"
        global sm
        sm = ScreenManager()

        sm.add_widget(Builder.load_file("signup.kv"))
        sm.add_widget(Builder.load_file("notification.kv"))
        sm.add_widget(Builder.load_file("addemp.kv"))
        return sm

    def send_to_admin(self,):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        # create a cursor
        c = mydb.cursor()

        names = c.execute("SELECT name FROM test9")

        c.execute()
        mydb.commit()
        mydb.close()



LeavesystemApp().run()