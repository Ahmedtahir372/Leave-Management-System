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

        sm.add_widget(Builder.load_file('button.kv'))
        sm.add_widget(Builder.load_file('test12.kv'))
        sm.add_widget(Builder.load_file('add_employee_details.kv'))

        return sm

    def on_click_show_list(self):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()

        # Retrieve the employee data
        c.execute("SELECT Name, Phone_Number FROM test9")
        rows = c.fetchall()

        # Create the employee list
        employee_list = self.root.get_screen('emp_list').ids.container
        employee_list.clear_widgets()  # Clear existing widgets before populating the list
        for row in rows:
            # Create a TwoLineListItem with the employee name as text and phone number as secondary text
            item = TwoLineListItem(text=row[0], secondary_text=str(row[1]))
            # Bind the on_release event to the show_employee_details function
            item.bind(on_release=self.show_employee_details)
            # Add the TwoLineListItem to the employee list
            employee_list.add_widget(item)

    def show_employee_details(self, item):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()

        # Retrieve the employee details
        c.execute("SELECT * FROM test9 WHERE Phone_Number=%s", (item.secondary_text,))
        row = c.fetchone()
        sm.current = 'emp_detail'

        # Update the employee details screen with the retrieved data
        employee_details_screen = sm.get_screen('emp_detail')
        if employee_details_screen:
            print(str(row[0]))
            employee_details_screen.ids.name.text = str(row[0])
            employee_details_screen.ids.email.text = str(row[1])
            employee_details_screen.ids.phone.text = str(row[2])
            employee_details_screen.ids.gender.text = str(row[6])
            employee_details_screen.ids.dept.text = str(row[7])
            employee_details_screen.ids.desig.text = str(row[8])








MyApp().run()
