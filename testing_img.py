from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
import mysql.connector
from kivymd.uix.list import TwoLineListItem
import random
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from datetime import datetime
from kivymd.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle


Window.size = (310,570)


""",red,pink, 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 
'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']"""

class LeavesystemApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette = "Cyan"
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        # create a cursor
        c = mydb.cursor()

        mydb.commit()

        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("employee_leave_details.kv"))
        return sm

    def acreq(self,):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()
        det = sm.get_screen('emp_leave_details')
        global l, n
        if emp_type == "Teaching Employee":
            l = 'teaching_leave_record'
            n = 'teaching_records'
        elif emp_type == "Non-Teaching Employee":
            l = 'non_teaching_leave_record'
            n = 'non_teaching_records'
        else:
            dialog = MDDialog(
                title='Warning',
                text=f"Select Employee type"
            )
            dialog.open()


        mydb.commit()
        mydb.close()


LeavesystemApp().run()


