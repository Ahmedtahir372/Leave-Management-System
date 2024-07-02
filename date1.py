from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
import mysql.connector
from datetime import datetime

Window.size = (310,570)
class dateincreaseApp(MDApp):
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

        # create actual db

        # create a secondary table to store employee records
        c.execute("""CREATE TABLE if not exists Date_test(Employee_ID INT PRIMARY KEY,Casual_Leave INT,Medical_Leave INT,Earned_Leave INT,Child_Care_Leave INT,Maternity_Leave INT,Duty_Leave INT,Sick_Leave INT, last_updated DATE)""")
        mydb.commit()
        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("button.kv"))
        return sm

    def increment(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        tup = (0,)
        tap =0
        # create a cursor
        c = mydb.cursor()
        current_date = datetime.now().date()

        c.execute("SELECT Employee_ID FROM Date_test")
        row = c.fetchall()
        for i in row:
            c.execute("SELECT last_updated from Date_test WHERE Employee_ID = %s ", i)
            last_updated_date = c.fetchone()
            if (current_date - last_updated_date[0]).days >= 365:
                c.execute("UPDATE Date_test SET Earned_Leave = Earned_Leave + 10 WHERE Employee_ID = %s", i)
                c.execute("UPDATE Date_test SET Casual_Leave = 12 WHERE Employee_ID = %s", i)
                tup = i
                tap = int(tup[0])

                last_updated_date = current_date
                c.execute("UPDATE date_test SET last_updated = %s WHERE Employee_ID = %s",(last_updated_date,tap))
                mydb.commit()




dateincreaseApp().run()