from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
import mysql.connector
from kivymd.uix.list import TwoLineListItem
import random
from kivy.clock import Clock



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

        # create actual db

        # create a secondary table to store employee records
        c.execute("""CREATE TABLE if not exists test_9(Employee_ID INT PRIMARY KEY, Name VARCHAR(100),email_ID VARCHAR(100) ,Phone_Number NUMERIC(14) ,password VARCHAR(20),Joining_Date DATE,Post VARCHAR(30),Gender VARCHAR(10) ,Department VARCHAR(30),Designation VARCHAR(30))""")
        c.execute("""CREATE TABLE if not exists Teaching_records (Employee_ID INT PRIMARY KEY, Name VARCHAR(100),email_ID VARCHAR(100) ,Phone_Number NUMERIC(14) ,password VARCHAR(20),Joining_Date DATE,Post VARCHAR(30),Gender VARCHAR(10) ,Department VARCHAR(30),Designation VARCHAR(30))""")
        c.execute("""CREATE TABLE if not exists Non_Teaching_Records (Employee_ID INT PRIMARY KEY, Name VARCHAR(100),email_ID VARCHAR(100) ,Phone_Number NUMERIC(14) ,password VARCHAR(20),Joining_Date DATE,Post VARCHAR(30),Gender VARCHAR(10) ,Department VARCHAR(30),Designation VARCHAR(30))""")



        #Leave tables
        c.execute("""CREATE TABLE if not exists Teaching_leave1(ID INT,Name VARCHAR(50),Leave_type VARCHAR(100),emp_type VARCHAR(40),From_Date DATE,To_Date DATE,reason VARCHAR(30))""")
        c.execute("""CREATE TABLE if not exists Non_Teaching_leave2(ID INT,Name VARCHAR(50),Leave_type VARCHAR(100),emp_type VARCHAR(100),From_Date DATE,To_Date DATE,reason VARCHAR(100))""")

        mydb.commit()

        global sm
        sm = ScreenManager()

        sm.add_widget(Builder.load_file("splash.kv"))
        sm.add_widget(Builder.load_file("login.kv"))
        sm.add_widget(Builder.load_file("signup.kv"))
        sm.add_widget(Builder.load_file("teaching_dashboard.kv"))
        sm.add_widget(Builder.load_file("non_teaching_dashboard.kv"))
        sm.add_widget(Builder.load_file("admin_dashboard.kv"))
        sm.add_widget(Builder.load_file("employees_list.kv"))
        sm.add_widget(Builder.load_file("add_employee_details.kv"))
        sm.add_widget(Builder.load_file("Leave_request.kv"))
        sm.add_widget(Builder.load_file("leave_list.kv"))
        sm.add_widget(Builder.load_file("employee_leave_details.kv"))
        sm.add_widget(Builder.load_file("check_balance.kv"))
        sm.add_widget(Builder.load_file("check_balance_empid.kv"))
        sm.add_widget(Builder.load_file("check_balance_empid1.kv"))
        sm.add_widget(Builder.load_file("update_profile.kv"))




        sm.add_widget(Builder.load_file("test_appdrawer.kv"))

        sm.add_widget(Builder.load_file("admin.kv"))
        sm.add_widget(Builder.load_file("teaching.kv"))
        sm.add_widget(Builder.load_file("non-teaching.kv"))


        sm.add_widget(Builder.load_file("view_edit_leave_request.kv"))
        sm.add_widget(Builder.load_file("teaching_Leave_request.kv"))
        sm.add_widget(Builder.load_file("view_leave_balance.kv"))



        return sm





    def on_start(self):
        # Schedule a function to be called after 3 seconds
        Clock.schedule_once(self.next_screen, 10)
    def next_screen(self,dt):
        MDApp.get_running_app().root.current = 'login'





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
        rand_num = random.randint(1, 100000)
        c.execute(f"insert into test_9 values('{rand_num}','{full_name.text}','{email_id.text}','{phone_no.text}','{password.text}','{jdate.text}','{spinner_id1.text}','{spinner_id2.text}','{spinner_id3.text}','{spinner_id4.text}')")
        c.execute(f"insert into date_test values('{rand_num}',0,0,0,0,0,0,0,'{jdate.text}')")
        mydb.commit()
        mydb.close()


    #function for employee list
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
        c.execute("SELECT Name, Employee_ID FROM test_9")
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

    #function to show employee list on click
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
        c.execute("SELECT * FROM test_9 WHERE Employee_ID=%s", (item.secondary_text,))
        row = c.fetchone()
        sm.current = 'emp_detail'

        # Update the employee details screen with the retrieved data
        employee_details_screen = sm.get_screen('emp_detail')
        if employee_details_screen:

            employee_details_screen.ids.name.text = str(row[1])
            employee_details_screen.ids.email.text = str(row[2])
            employee_details_screen.ids.phone.text = str(row[3])
            employee_details_screen.ids.gender.text = str(row[7])
            employee_details_screen.ids.emp_type.text = str(row[6])
            employee_details_screen.ids.dept.text = str(row[8])
            employee_details_screen.ids.desig.text = str(row[9])

    ##function for employee list
    def on_click_show_list_from_primary_table(self):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()

        # Retrieve the employee data
        c.execute("SELECT Name, Phone_Number FROM test_pr")
        rows = c.fetchall()

        # Create the employee list
        employee_list = self.root.get_screen('emp_list').ids.container
        employee_list.clear_widgets()  # Clear existing widgets before populating the list
        for row in rows:
            # Create a TwoLineListItem with the employee name as text and phone number as secondary text
            item = TwoLineListItem(text=row[0], secondary_text=str(row[1]))
            # Bind the on_release event to the show_employee_details function
            item.bind(on_release=self.show_employee_details_from_primary_table)
            # Add the TwoLineListItem to the employee list
            employee_list.add_widget(item)


    ##function to show employee list on click
    def show_employee_details_from_primary_table(self, item):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()

        # Retrieve the employee details
        c.execute("SELECT * FROM test_pr WHERE Phone_Number=%s", (item.secondary_text,))
        row = c.fetchone()
        sm.current = 'emp_detail'

        # Update the employee details screen with the retrieved data
        employee_details_screen = sm.get_screen('emp_detail')
        if employee_details_screen:

            employee_details_screen.ids.name.text = str(row[0])
            employee_details_screen.ids.email.text = str(row[1])
            employee_details_screen.ids.phone.text = str(row[2])
            employee_details_screen.ids.gender.text = str(row[6])
            employee_details_screen.ids.dept.text = str(row[7])
            employee_details_screen.ids.desig.text = str(row[8])




    #function to add employee(for admin section)
    def add_emp(self,phone,emp_type):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()
        if emp_type =="Teaching":
            c.execute("DELETE FROM non_teaching WHERE Phone_Number =%s", (phone.text,))
        else:
            c.execute("DELETE FROM teaching1 WHERE Phone_Number =%s", (phone.text,))
        c.execute("DELETE FROM test9 WHERE Phone_Number =%s", (phone.text,))
        MDApp.get_running_app().root.current = 'emp_list'

        mydb.commit()
        mydb.close()



    #function to remove employee(for admin section)
    def rem_emp(self,phone):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()
        c.execute("DELETE FROM test9 WHERE Phone_Number =%s", (phone.text,))
        c.execute("DELETE FROM test_pr WHERE Phone_Number =%s", (phone.text,))

        MDApp.get_running_app().root.current = 'emp_list'

        mydb.commit()
        mydb.close()



          mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()


        # Retrieve the employee data
        c.execute("SELECT name, ID FROM Non_Teaching_leave2")

        rows = c.fetchall()


        # Create the teaching employee leave list
        leave_list = self.root.get_screen('leave_list').ids.container1
        leave_list.clear_widgets()  # Clear existing widgets before populating the list
        for row in rows:
            # Create a TwoLineListItem with the employee name as text and phone number as secondary text
            item = TwoLineListItem(text=row[0], secondary_text=str(row[1]))
            # Bind the on_release event to the show_employee_details function
            item.bind(on_release=self.show_employee_details)
            # Add the TwoLineListItem to the employee list
            leave_list.add_widget(item)







LeavesystemApp().run()