from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import MDList, OneLineListItem
import mysql.connector

class EmployeeListItem(OneLineListItem):
    pass

class MyApp(MDApp):
    def build(self):

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )

        # Load the .kv files
        Builder.load_file('employee_list.kv')
        Builder.load_file('employee_details.kv')

        # Create and configure the ScreenManager
        self.screen_manager = Builder.load_file('screen_manager.kv')
        self.screen_manager.transition.direction = 'left'

        # Connect to the database

        c = mydb.cursor()

        # Retrieve the employee names
        c.execute("SELECT name FROM test9")
        rows = c.fetchall()

        # Create the employee list
        employee_list = self.screen_manager.get_screen('employee_list_screen').ids.employee_list
        for row in rows:
            employee_list.add_widget(EmployeeListItem(text=row[0]))

        return self.screen_manager

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
        c.execute("SELECT * FROM employees WHERE name=?", (item.text,))
        row = c.fetchone()

        # Update the employee details screen with the retrieved data
        employee_details_screen = self.screen_manager.get_screen('employee_details_screen')
        employee_details_screen.ids.name_label.text = row[0]
        employee_details_screen.ids.age_label.text = row[1]
        employee_details_screen.ids.department_label.text = row[2]

MyApp().run()
