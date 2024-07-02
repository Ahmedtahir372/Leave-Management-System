from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem
import mysql.connector
from kivy.core.window import Window

Window.size = (310,570)

class MyApp(MDApp):
    def build(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()
        # Load the .kv files
        global sm
        sm = ScreenManager()


        sm.add_widget(Builder.load_file('signup.kv'))


        return sm

    def signup(self,full_name,email_id,phone_no,password,jdate,spinner_id1,spinner_id2,spinner_id3,spinner_id4):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        # create a cursor
        c = mydb.cursor()
        #insert_record
        #secondary table
        c.execute(f"insert into test9 values('{full_name.text}','{email_id.text}','{phone_no.text}','{password.text}','{jdate.text}','{spinner_id1.text}','{spinner_id2.text}','{spinner_id3.text}','{spinner_id4.text}')")
        mydb.commit()
        mydb.close()




MyApp().run()
