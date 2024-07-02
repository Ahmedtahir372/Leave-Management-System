from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
import mysql.connector
from kivymd.uix.list import TwoLineListItem


Window.size = (310, 570)



class LeavesystemApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
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

        #  Leave table for teaching employee
        c.execute("""CREATE TABLE if not exists Teaching_leave1(ID INT,Name VARCHAR(50),Leave_type VARCHAR(100),emp_type VARCHAR(40),From_Date DATE,To_Date DATE,reason VARCHAR(30))""")

        #  Leave table for teaching employee
        c.execute("""CREATE TABLE if not exists Non_Teaching_leave2(ID INT,Name VARCHAR(50),Leave_type VARCHAR(100),emp_type VARCHAR(100),From_Date DATE,To_Date DATE,reason VARCHAR(100))""")
        mydb.commit()
        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("admin_dashboard.kv"))
        sm.add_widget(Builder.load_file("leave_list.kv"))
        sm.add_widget(Builder.load_file("employee_leave_details.kv"))
        return sm

    def send_request(self,name,leave_types,emp_type,fdate,tdate,reason):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        # create a cursor
        c = mydb.cursor()

        if emp_type == "Teaching Employee":
            c.execute(f"INSERT INTO Teaching_leave1 VALUES(RAND()*1000,'{name}','{leave_types}','{emp_type}','{fdate}','{tdate}','{reason}')")

        elif emp_type == "Non-Teaching Employee":
            c.execute(f"INSERT INTO Non_Teaching_leave2 VALUES(RAND()*1000,'{name}','{leave_types}','{emp_type}','{fdate}','{tdate}','{reason}')")

        mydb.commit()

    #function for employee list
    def on_click_teaching_leave_list(self):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()


        # Retrieve the employee data
        c.execute("SELECT ID, name FROM Teaching_leave1")

        rows = c.fetchall()


        # Create the teaching employee leave list
        leave_list = self.root.get_screen('leave_list').ids.container
        leave_list.clear_widgets()  # Clear existing widgets before populating the list
        for row in rows:
            # Create a TwoLineListItem with the employee name as text and phone number as secondary text
            item = TwoLineListItem(text=str(row[1]), secondary_text=str(row[0]))
            # Bind the on_release event to the show_employee_details function

            item.bind(on_release=self.show_temployee_leave_details)
            # Add the TwoLineListItem to the employee list
            leave_list.add_widget(item)

    #function for employee list
    def on_click_non_teaching_leave_list(self):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()


        # Retrieve the employee data
        c.execute("SELECT ID, name FROM Non_Teaching_leave2")

        rows = c.fetchall()


        # Create the teaching employee leave list
        leave_list = self.root.get_screen('leave_list').ids.container1
        leave_list.clear_widgets()  # Clear existing widgets before populating the list
        for row in rows:
            # Create a TwoLineListItem with the employee name as text and phone number as secondary text
            item = TwoLineListItem(text=str(row[1]), secondary_text=str(row[0]))
            # Bind the on_release event to the show_employee_details function
            item.bind(on_release=self.show_nemployee_leave_details)
            # Add the TwoLineListItem to the employee list
            leave_list.add_widget(item)


    def show_nemployee_leave_details(self, item):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()

        # Retrieve the employee details
        c.execute("SELECT * FROM Non_Teaching_leave2 WHERE ID = %s", (item.secondary_text,))
        row = c.fetchone()

        sm.current = 'emp_leave_details'

        # Update the employee details screen with the retrieved data
        employee_details_screen = sm.get_screen('emp_leave_details')


        employee_details_screen.ids.ltype.text = str(row[2])
        employee_details_screen.ids.emp_type.text = str(row[3])
        employee_details_screen.ids.name.text = str(row[1])
        employee_details_screen.ids.fdate.text = str(row[4])
        employee_details_screen.ids.tdate.text = str(row[5])
        employee_details_screen.ids.reason.text = str(row[6])



    def show_temployee_leave_details(self, item):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()

        # Retrieve the employee details
        c.execute("SELECT * FROM Teaching_leave1 WHERE ID = %s", (item.secondary_text,))
        row = c.fetchone()

        sm.current = 'emp_leave_details'


        # Update the employee details screen with the retrieved data
        employee_details_screen = sm.get_screen('emp_leave_details')


        employee_details_screen.ids.ltype.text = str(row[2])
        employee_details_screen.ids.emp_type.text = str(row[3])
        employee_details_screen.ids.name.text = str(row[1])
        employee_details_screen.ids.fdate.text = str(row[4])
        employee_details_screen.ids.tdate.text = str(row[5])
        employee_details_screen.ids.reason.text = str(row[6])


LeavesystemApp().run()
