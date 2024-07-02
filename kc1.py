from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
import mysql.connector
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.list import TwoLineListItem
import random
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from datetime import datetime
from kivymd.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
import re
from kivymd.uix.filemanager import MDFileManager
from io import BytesIO
from PIL import Image
from kivymd.uix.textfield import MDTextField
import smtplib
from kivymd.uix.dialog import MDDialog
import threading as th
from kivymd.uix.button import MDFlatButton



Window.size = (310,570)


""",red,pink, 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 
'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']"""

class LeavesystemApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path,
        )
        self.file_mana = MDFileManager(
            exit_manager=self.exit_file_mana,
            select_path=self.select_pa,
        )



    def build(self):
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette = "Cyan"
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        # create a cursor
        c = mydb.cursor()

        # create actual db

        # create a secondary table to store employee records
        c.execute("""CREATE TABLE if not exists secondary_table(Employee_ID VARCHAR(50) PRIMARY KEY, Name VARCHAR(100),email_ID VARCHAR(100) ,Phone_Number NUMERIC(14) ,password VARCHAR(20),Joining_Date DATE,Post VARCHAR(30),Gender VARCHAR(10) ,Department VARCHAR(30),Designation VARCHAR(30))""")
        c.execute("""CREATE TABLE if not exists Teaching_records (Employee_ID VARCHAR(50) PRIMARY KEY, Name VARCHAR(100),email_ID VARCHAR(100) ,Phone_Number NUMERIC(14) ,password VARCHAR(20),Joining_Date DATE,Post VARCHAR(30),Gender VARCHAR(10) ,Department VARCHAR(30),Designation VARCHAR(30))""")
        c.execute("""CREATE TABLE if not exists Non_Teaching_Records (Employee_ID VARCHAR(50) PRIMARY KEY, Name VARCHAR(100),email_ID VARCHAR(100) ,Phone_Number NUMERIC(14) ,password VARCHAR(20),Joining_Date DATE,Post VARCHAR(30),Gender VARCHAR(10) ,Department VARCHAR(30),Designation VARCHAR(30))""")
        c.execute("""CREATE TABLE if not exists Admin_Records (Employee_ID VARCHAR(50) PRIMARY KEY, Name VARCHAR(100),email_ID VARCHAR(100) ,Phone_Number NUMERIC(14) ,password VARCHAR(20),Joining_Date DATE,Post VARCHAR(30),Gender VARCHAR(10) ,Department VARCHAR(30),Designation VARCHAR(30))""")

        #Leave tables
        c.execute("""CREATE TABLE if not exists Teaching_leave_record(Employee_ID VARCHAR(50) UNIQUE,Name VARCHAR(50),Leave_type VARCHAR(100),emp_type VARCHAR(40),From_Date DATE,To_Date DATE,reason VARCHAR(30))""")
        c.execute("""CREATE TABLE if not exists Non_Teaching_leave_record(Employee_ID VARCHAR(50) UNIQUE,Name VARCHAR(50),Leave_type VARCHAR(100),emp_type VARCHAR(100),From_Date DATE,To_Date DATE,reason VARCHAR(100))""")

        #Leave Balance
        c.execute("""CREATE TABLE if not exists Leave_Balance(Employee_ID VARCHAR(50) PRIMARY KEY,Casual_Leave INT,Earned_Leave INT,last_updated DATE)""")

        #notice
        c.execute("CREATE TABLE if not exists notice(Employee_ID VARCHAR(50) ,Sentence VARCHAR(100))")
        #employee photo table
        c.execute("CREATE TABLE if not exists dp(Employee_ID VARCHAR(50) ,pic LONGBLOB)")
        # employee birth certificate photo table
        c.execute("CREATE TABLE if not exists the_captured_image(Employee_ID VARCHAR(50) ,the_image LONGBLOB)")

        #leave history table
        c.execute("""CREATE TABLE if not exists leave_history(Employee_ID VARCHAR(50),Name VARCHAR(50),Leave_type VARCHAR(100),emp_type VARCHAR(40),From_Date DATE,To_Date DATE,reason VARCHAR(30),eventtime DATETIME)""")
        mydb.commit()

        global sm
        sm = ScreenManager()

        sm.add_widget(Builder.load_file("splash.kv"))
        sm.add_widget(Builder.load_file("new_log3.kv"))
        sm.add_widget(Builder.load_file("new_signup2.kv"))
        sm.add_widget(Builder.load_file("new_teaching_dashboard.kv"))
        sm.add_widget(Builder.load_file("new_non_teaching_dashboard.kv"))
        sm.add_widget(Builder.load_file("new_admin_dashboard.kv"))
        sm.add_widget(Builder.load_file("employees_list.kv"))
        sm.add_widget(Builder.load_file("add_employee_details.kv"))
        sm.add_widget(Builder.load_file("Leave_request.kv"))
        sm.add_widget(Builder.load_file("leave_list.kv"))
        sm.add_widget(Builder.load_file("employee_leave_details.kv"))
        sm.add_widget(Builder.load_file("check_balance.kv"))
        sm.add_widget(Builder.load_file("check_balance_empid.kv"))
        sm.add_widget(Builder.load_file("check_balance_empid1.kv"))
        sm.add_widget(Builder.load_file("update_profile.kv"))
        sm.add_widget(Builder.load_file("notice.kv"))
        sm.add_widget(Builder.load_file("notice2.kv"))
        sm.add_widget(Builder.load_file("Leave_request_edit.kv"))
        sm.add_widget(Builder.load_file("upload_certificate.kv"))
        sm.add_widget(Builder.load_file("noticelist.kv"))
        sm.add_widget(Builder.load_file("leave_con_report.kv"))
        sm.add_widget(Builder.load_file("details_of_employee.kv"))
        sm.add_widget(Builder.load_file("show_document.kv"))
        sm.add_widget(Builder.load_file("test_appdrawer.kv"))
        sm.add_widget(Builder.load_file("leave_history_list.kv"))

        return sm





    def on_start(self):
        # Schedule a function to be called after 3 seconds
        Clock.schedule_once(self.next_screen, 16)
    def next_screen(self,dt):
        MDApp.get_running_app().root.current = 'login'

    '''def send_email(self, *args):
        
        
        
        
        try:
            # Get the email details from the text fields
            email = "jr1954674@gmail.com"
            password = "eysdmzhuxvuenezz"
            recipient = .text
            subject =" OTP"
            message = rand

            # Connect to the email server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.ehlo()
            server.login(email, password)

            # Compose the email
            email_message = f"Subject: {subject}\n\n{message}"

            # Send the email
            server.sendmail(email, recipient, email_message)
            server.quit()

        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Warning',
                text=f"{e}"
            )
            dialog.open()'''








    def verify_otp(self,):

        try:
            rand = str(random.randint(100000, 999999))
            det= sm.get_screen('signup')
            # Get the email details from the text fields
            email = "jr1954674@gmail.com"
            password = "eysdmzhuxvuenezz"
            recipient = det.ids.email_id.text
            subject =" OTP"
            message = rand

            # Connect to the email server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.ehlo()
            server.login(email, password)

            # Compose the email
            email_message = f"Subject: {subject}\n\n{message}"

            # Send the email
            server.sendmail(email, recipient, email_message)
            server.quit()

            dialo = MDDialog(
                title="Enter the OTP sent to you",
                type="custom",
                content_cls=MDTextField(hint_text="Enter OTP", size_hint=(None, None), width=280),
                buttons=[
                    MDFlatButton(text="Cancel", on_release=lambda *args: dialo.dismiss()),
                    MDFlatButton(text="OK",
                                 on_release=lambda *args: self.process_input(rand, dialo.content_cls.text, dialo)),
                ],
            )

            dialo.open()
        except Exception as e:
            dialog = MDDialog(
                title='Warning',
                text="Enter the data correctly"
            )
            dialog.open()





    '''def send_by_thread(self):
        
        det = sm.get_screen('signup')

        recipient = det.ids.email_id.text

        # Start a new thread to send the email
        t1 = th.Thread(
            target=self.verify_otp,
            args=(recipient,),
        )
        t1.start()'''


    def process_input(self, rand, otp, dialo):
        print(rand, otp)
        try:
            if otp == rand:
                print("continue")
                dialog = MDDialog(
                    title='Notice',
                    text="Your emeail is verified"
                )
                dialog.open()
                # close another dialog from here
                dialo.dismiss()

            else:
                dialog = MDDialog(
                    title='Warning',
                    text="Wrong OTP"
                )
            dialog.open()

        except Exception as e:
            dialog = MDDialog(
                title='NOtice',
                text="Sorry an unknown error occured"
            )
            dialog.open()

    def leave_history_list(self):
        print("running")
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()
        global u, empid
        c = mydb.cursor()
        det = sm.get_screen('login')
        t = det.ids.login_as.text
        if t == "Teaching Employee":
            u = sm.get_screen('teaching_dashboard')
            empid = u.ids.tea.text

        if t == "Non-Teaching Employee":
            u = sm.get_screen('non_teaching_dashboard')
            empid = u.ids.non_tea.text


        # Retrieve the employee data
        c.execute("SELECT Name, Employee_ID,eventtime FROM leave_history WHERE Employee_ID =%s",(empid,))
        row = c.fetchone()

        current_date = row[2]
        formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
        sm.current = 'leave_history_list'


        # Create the teaching employee leave list
        leave_list = self.root.get_screen('leave_history_list').ids.container
        leave_list.clear_widgets()  # Clear existing widgets before populating the list
        for ro in row:
            # Create a TwoLineListItem with the employee name as text and phone number as secondary text
            item = ThreeLineListItem(text=ro[0],secondary_text=str(ro[1]),tertiary_text=str(formatted_date))
            # Bind the on_release event to the show_employee_details function
            item.bind(on_release=self.leave_history_details)
            # Add the TwoLineListItem to the employee list
            leave_list.add_widget(item)

    def leave_history_details(self, item):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()

        # Retrieve the employee details
        c.execute("SELECT * FROM leave_history WHERE Employee_ID = %s AND eventtime=%s", (item.secondary_text,item.tertiary_text))
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
        employee_details_screen.ids.empid.text = item.secondary_text

    def dashboard_details(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        # create a cursor
        c = mydb.cursor()

        global u, empid
        c = mydb.cursor()
        det = sm.get_screen('login')
        t = det.ids.login_as.text
        if t == "Teaching Employee":
            u = sm.get_screen('teaching_dashboard')
            empid = u.ids.tea.text

        if t == "Non-Teaching Employee":
            u = sm.get_screen('non_teaching_dashboard')
            empid = u.ids.non_tea.text

        if t == "Admin":
            u = sm.get_screen('admin_dashboard')
            empid = u.ids.admin.text
        c.execute("SELECT the_image FROM the_captured_image WHERE Employee_ID = %s",(empid,))
        row = c.fetchone()
        if row is None:
            print("none")
        else:
            image_data = row[0]
            image = Image.open(BytesIO(image_data))
            image.save("temp_image.jpg")
            det = sm.get_screen('admin_dashboard')

            det.ids.name.text = "hey"
            det.ids.empid.text = "hey"
            det.ids.email.text = "hey"
            det.ids.phone.text = "hey"
            det.ids.jdate.text = "hey"
            det.ids.my_image.source = 'temp_image.jpg'


    def open_file_manager(self):
        self.file_manager.show('/')  # Show the file manager starting from the root directory

    def select_path(self, path):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        dete=sm.get_screen('Leave_Request_Form')
        emp = dete.ids.empid.text
        self.cursor = self.mydb.cursor()
        # Handle the selected image file path here
        self.file_manager.close()
        print("Selected File:", path)
        det = sm.get_screen('certificate')
        det.ids.my_image.source = path
        with open(path, 'rb') as image_file:
            img = image_file.read()
            self.cursor.execute("SELECT * FROM the_captured_image WHERE Employee_ID=%s",(emp,))
            row = self.cursor.fetchone()
            if row is None:
                self.cursor.execute("INSERT INTO the_captured_image VALUES(%s,%s)", (emp,img))
            else:

                sql = "UPDATE the_captured_image SET the_image = %s WHERE Employee_ID = %s"
                self.cursor.execute(sql, (img,emp))
            self.mydb.commit()

    def exit_file_manager(self, *args):
        self.file_manager.close()




    def open_file_mana(self):
        self.file_mana.show('/')  # Show the file manager starting from the root directory

    def select_pa(self, path):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        global det,emp
        self.cursor = self.mydb.cursor()
        # Handle the selected image file path here
        self.file_mana.close()
        print("Selected File:", path)
        if sm.current=='admin_dashboard':
            det = sm.get_screen('admin_dashboard')
            emp = det.ids.admin.text
        if sm.current =='teaching_dashboard':
            det = sm.get_screen('teaching_dashboard')
            emp = det.ids.tea.text
        if sm.current =='non_teaching_dashboard':
            det = sm.get_screen('non_teaching_dashboard')
            emp = det.ids.non_tea.text

        det.ids.my_image.source = path
        with open(path, 'rb') as image_file:
            img = image_file.read()
            self.cursor.execute("SELECT Employee_ID FROM dp WHERE Employee_ID=%s", (emp,))
            row = self.cursor.fetchone()
            if row is None:
                self.cursor.execute("INSERT INTO dp VALUES(%s,%s)", (emp, img))
            else:
                sql = "UPDATE dp SET pic = %s WHERE Employee_ID = %s"
                self.cursor.execute(sql, (img, emp))
            self.mydb.commit()
    def exit_file_mana(self, *args):
        self.file_mana.close()




    def show_dp(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        global det,emp,t
        self.cursor = self.mydb.cursor()
        # Handle the selected image file path here


        if sm.current =='admin_dashboard':
            det = sm.get_screen('admin_dashboard')
            emp = det.ids.admin.text
            t = "admin_records"

            self.cursor.execute("SELECT * FROM {} WHERE Employee_ID = %s".format(t), (emp,))
            ray = self.cursor.fetchone()
            det.ids.name.text = str(ray[1])
            det.ids.empid.text = str(ray[0])
            det.ids.email.text = str(ray[2])
            det.ids.phone.text = str(ray[3])
            det.ids.jdate.text = str(ray[5])
            self.cursor.execute("SELECT pic FROM dp WHERE Employee_ID = %s", (emp,))
            row = self.cursor.fetchone()
            if row is None:
                pass

            else:
                image_data = row[0]
                image = Image.open(BytesIO(image_data))
                image.save("temp_image.jpg")
                det.ids.my_image.source = 'temp_image.jpg'

        if sm.current =='teaching_dashboard':
            det = sm.get_screen('teaching_dashboard')
            emp = det.ids.tea.text
            t = "teaching_records"

            self.cursor.execute("SELECT * FROM {} WHERE Employee_ID = %s".format(t), (emp,))
            ray = self.cursor.fetchone()
            det.ids.name.text=str(ray[1])
            det.ids.empid.text=str(ray[0])
            det.ids.email.text=str(ray[2])
            det.ids.phone.text=str(ray[3])
            det.ids.jdate.text=str(ray[5])
            det.ids.dept.text=str(ray[9])
            det.ids.desig.text=str(ray[8])
            self.cursor.execute("SELECT pic FROM dp WHERE Employee_ID = %s", (emp,))
            row = self.cursor.fetchone()
            if row is None:
                pass

            else:
                image_data = row[0]
                image = Image.open(BytesIO(image_data))
                image.save("temp_image.jpg")
                det.ids.my_image.source = 'temp_image.jpg'

        if sm.current =='non_teaching_dashboard':
            det = sm.get_screen('non_teaching_dashboard')
            emp = det.ids.non_tea.text
            t = "non_teaching_records"
            self.cursor.execute("SELECT * FROM {} WHERE Employee_ID = %s".format(t), (emp,))
            ray = self.cursor.fetchone()
            det.ids.name.text=str(ray[1])
            det.ids.empid.text=str(ray[0])
            det.ids.email.text=str(ray[2])
            det.ids.phone.text=str(ray[3])
            det.ids.jdate.text=str(ray[5])
            det.ids.dept.text=str(ray[9])
            det.ids.desig.text=str(ray[8])


            self.cursor.execute("SELECT pic FROM dp WHERE Employee_ID = %s",(emp,))
            row = self.cursor.fetchone()
            if row is None:
                pass

            else:
                image_data = row[0]
                image = Image.open(BytesIO(image_data))
                image.save("temp_image.jpg")
                det.ids.my_image.source = 'temp_image.jpg'




    def show_document(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        dete = sm.get_screen('emp_leave_details')
        emp = dete.ids.empid.text
        # create a cursor
        c = mydb.cursor()
        c.execute("SELECT the_image FROM the_captured_image WHERE Employee_ID = %s",(emp,))
        row = c.fetchone()
        if row is None:
            dialog = MDDialog(
                title='Notice',
                text="No attached document"
            )
            dialog.open()

        else:
            image_data = row[0]
            image = Image.open(BytesIO(image_data))
            image.save("temp_image.jpg")
            sm.current = 'show_doc'
            det = sm.get_screen('show_doc')
            det.ids.my_image.source = 'temp_image.jpg'







    #function for employee list
    def notice_list(self,):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        global u,empid
        c = mydb.cursor()
        det = sm.get_screen('login')
        t = det.ids.login_as.text
        if t == "Teaching Employee":
            u = sm.get_screen('teaching_dashboard')
            empid=u.ids.tea.text

        if t == "Non-Teaching Employee":
            u = sm.get_screen('non_teaching_dashboard')
            empid=u.ids.non_tea.text




        # Retrieve the employee data
        c.execute("SELECT Employee_ID,Name,eventtime FROM leave_history WHERE Employee_ID = %s",(empid,))
        print("li",empid)
        row = c.fetchone()
        if row is None:
            dialog = MDDialog(
                title='Notice',
                text="You don't have any notice"
            )
            dialog.open()
        else:
            sm.current='noticelist'

            # Create the employee list
            employee_list = self.root.get_screen('noticelist').ids.container
            employee_list.clear_widgets()  # Clear existing widgets before populating the list
            item = ThreeLineListItem(text=row[1],secondary_text=str(empid),tertiary_text=str(row[2]))
            # Bind the on_release event to the show_employee_details function
            item.bind(on_release=self.notice_details)
            # Add the TwoLineListItem to the employee list
            employee_list.add_widget(item)


    #function to show employee list on click
    def notice_details(self,item):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )

        global u, empid,row,term,ta
        det = sm.get_screen('login')
        t = det.ids.login_as.text
        if t == "Teaching Employee":
            u = sm.get_screen('teaching_dashboard')
            ta = "teaching_leave_record"
            empid = u.ids.tea.text

        if t == "Non-Teaching Employee":
            u = sm.get_screen('non_teaching_dashboard')
            ta = "non_teaching_leave_record"
            empid = u.ids.tea.text
        c = mydb.cursor()
        # Retrieve the employee details
        c.execute("SELECT sentence FROM notice WHERE Employee_ID=%s ", (item.secondary_text,))
        rat = c.fetchone()
        if rat[0]=="Accepted":
            term = "Your leave is sanctioned"
        else:
            term = "Your leave is rejected"

        c.execute("SELECT * FROM leave_history WHERE Employee_ID=%s AND eventtime = %s",(item.secondary_text,item.tertiary_text,))
        row = c.fetchone()
        print(row)
        print(empid)
        print(item.secondary_text)


        sm.current = 'leave_con_report'

        # Update the employee details screen with the retrieved data
        employee_details_screen = sm.get_screen('leave_con_report')
        if employee_details_screen:

            employee_details_screen.ids.sen.text = term
            employee_details_screen.ids.empid.text = str(row[0])
            employee_details_screen.ids.name.text = str(row[1])
            employee_details_screen.ids.ltype.text = str(row[2])
            employee_details_screen.ids.emp_type.text = str(row[3])
            employee_details_screen.ids.fdate.text = str(row[4])
            employee_details_screen.ids.tdate.text = str(row[5])
            employee_details_screen.ids.reason.text = str(row[6])

    #function for employee list
    def history_list(self,):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        global u,empid
        c = mydb.cursor()
        det = sm.get_screen('login')
        t = det.ids.login_as.text
        if t == "Teaching Employee":
            u = sm.get_screen('teaching_dashboard')
            empid=u.ids.tea.text

        if t == "Non-Teaching Employee":
            u = sm.get_screen('non_teaching_dashboard')
            empid=u.ids.non_tea.text




        # Retrieve the employee data
        c.execute("SELECT Employee_ID,Name,eventtime FROM leave_history WHERE Employee_ID = %s",(empid,))
        print("li",empid)
        row = c.fetchone()
        if row is None:
            dialog = MDDialog(
                title='Notice',
                text="You don't have any leaves"
            )
            dialog.open()
        else:
            sm.current='leave_history_list'

            # Create the employee list
            employee_list = self.root.get_screen('leave_history_list').ids.container
            employee_list.clear_widgets()  # Clear existing widgets before populating the list
            item = ThreeLineListItem(text=row[1],secondary_text=str(empid),tertiary_text=str(row[2]))
            # Bind the on_release event to the show_employee_details function
            item.bind(on_release=self.history_details)
            # Add the TwoLineListItem to the employee list
            employee_list.add_widget(item)


    #function to show employee list on click
    def history_details(self,item):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )

        global u, empid,row,term,ta
        det = sm.get_screen('login')
        t = det.ids.login_as.text
        if t == "Teaching Employee":
            u = sm.get_screen('teaching_dashboard')
            ta = "teaching_leave_record"
            empid = u.ids.tea.text

        if t == "Non-Teaching Employee":
            u = sm.get_screen('non_teaching_dashboard')
            ta = "non_teaching_leave_record"
            empid = u.ids.tea.text
        c = mydb.cursor()
        # Retrieve the employee details
        c.execute("SELECT sentence FROM notice WHERE Employee_ID=%s ", (item.secondary_text,))
        rat = c.fetchone()
        if rat[0]=="Accepted":
            term = "Your leave is sanctioned"
        else:
            term = "Your leave is rejected"

        c.execute("SELECT * FROM leave_history WHERE Employee_ID=%s AND eventtime = %s",(item.secondary_text,item.tertiary_text,))
        row = c.fetchone()
        print(row)
        print(empid)
        print(item.secondary_text)


        sm.current = 'leave_con_report'

        # Update the employee details screen with the retrieved data
        employee_details_screen = sm.get_screen('leave_con_report')
        if employee_details_screen:

            employee_details_screen.ids.sen.text = term
            employee_details_screen.ids.empid.text = str(row[0])
            employee_details_screen.ids.name.text = str(row[1])
            employee_details_screen.ids.ltype.text = str(row[2])
            employee_details_screen.ids.emp_type.text = str(row[3])
            employee_details_screen.ids.fdate.text = str(row[4])
            employee_details_screen.ids.tdate.text = str(row[5])
            employee_details_screen.ids.reason.text = str(row[6])










    def selected(self, filename):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        det = sm.get_screen('Leave_Request_Form')
        emp = det.ids.empid.text
        print(emp)
        # create a cursor
        c = mydb.cursor()
        image_path = filename[0]
        try:
            with open(image_path, "rb") as image_file:
                image_blob = image_file.read()
                c.execute("SELECT * FROM the_captured_image WHERE Employee_ID = %s ",(emp,))
                row = c.fetchone()
                if row is None:
                    c.execute("INSERT INTO the_captured_image VALUES(%s,%s) ", (emp,image_blob,))
                else:
                    c.execute("UPDATE the_captured_image SET the_image= %s WHERE Employee_ID = 123", (image_blob,))
                mydb.commit()

        except FileNotFoundError:
            print("Image not found!")

    def show_apply_request(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()
        det = sm.get_screen('login')
        global s, empid, t
        e = det.ids.login_as.text

        if e == "Teaching Employee":
            details = sm.get_screen('teaching_dashboard')
            empid = details.ids.tea.text
            t = 'teaching_records'
        elif e == "Non-Teaching Employee":
            details = sm.get_screen('non_teaching_dashboard')
            empid = details.ids.non_tea.text
            t = 'non_teaching_records'

        c.execute("SELECT * FROM {} WHERE Employee_ID = %s".format(t), (empid,))
        row = c.fetchone()


        sm.current='Leave_Request_Form'
        det = sm.get_screen('Leave_Request_Form')
        print(row)

        det.ids.emp_type.text=str(row[6])
        det.ids.name.text=str(row[1])
        det.ids.empid.text=str(row[0])





    def show_edit_request(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()
        det = sm.get_screen('login')
        global s, empid, t
        e = det.ids.login_as.text

        if e == "Teaching Employee":
            details = sm.get_screen('teaching_dashboard')
            empid = details.ids.tea.text
            t = 'teaching_leave_record'
        elif e == "Non-Teaching Employee":
            details = sm.get_screen('non_teaching_dashboard')
            empid = details.ids.non_tea.text
            t = 'non_teaching_leave_record'

        c.execute("SELECT * FROM {} WHERE Employee_ID = %s".format(t), (empid,))
        row = c.fetchone()
        if row is None:
            dialog = MDDialog(
                title='Notice',
                text="Yoy didn't applied for any leave")
            dialog.open()


        else:
            sm.current='Leave_Request_edit'
            det = sm.get_screen('Leave_Request_edit')

            print(row)
            det.ids.leave_types.text=str(row[2])
            det.ids.emp_type.text=str(row[3])
            det.ids.name.text=str(row[1])
            det.ids.empid.text=str(row[0])
            det.ids.fdate.text=str(row[4])
            det.ids.tdate.text=str(row[5])
            det.ids.reason.text=str(row[6])


    def leave_req_update(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()

        try:

            det = sm.get_screen('Leave_Request_edit')
            lt = det.ids.leave_types.text
            et =  det.ids.emp_type.text
            na = det.ids.name.text
            ei = det.ids.empid.text
            fd = det.ids.fdate.text
            td = det.ids.tdate.text
            r = det.ids.reason.text
            print(lt,et,na,ei,fd,td,r)
            if et == "Teaching Employee":
                c.execute("UPDATE teaching_leave_record SET Leave_type = %s,From_Date = %s,To_Date = %s,reason = %s WHERE Employee_ID = %s",(lt,fd,td,r,ei))
                mydb.commit()
                mydb.close()

            else:
                c.execute("UPDATE non_teaching_leave_record SET Leave_type = %s,From_Date = %s,To_Date = %s,reason = %s WHERE Employee_ID = %s",(lt,fd,td,r,ei))
                mydb.commit()
                mydb.close()
        except Exception as e:
            print(e)



    def dialog1(self):
        dialog = MDDialog(
              title='Notice',
              text='You Can login after the admin accepts your request')
        dialog.open()



    def show_update_profile(self,):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()
        det = sm.get_screen('login')
        global s,empid,t
        e = det.ids.login_as.text

        if e == "Admin":
            details = sm.get_screen('admin_dashboard')
            empid = details.ids.admin.text
            t = 'admin_records'
        elif e == "Teaching Employee":
            details = sm.get_screen('teaching_dashboard')
            empid = details.ids.tea.text

            t ='teaching_records'
        elif e == "Non-Teaching Employee":
            details = sm.get_screen('non_teaching_dashboard')
            empid = details.ids.non_tea.text
            t = 'non_teaching_records'

        c.execute("SELECT * FROM {} WHERE Employee_ID = %s".format(t),(empid,))
        row = c.fetchone()
        sm.current = 'update'
        details_screen = sm.get_screen('update')
        if details_screen:
            details_screen.ids.empid.text = str(row[0])
            details_screen.ids.empid.disabled = True
            details_screen.ids.full_name.text = str(row[1])
            details_screen.ids.email_id.text = str(row[2])
            details_screen.ids.phone_no.text =str(row[3])
            details_screen.ids.password.text =str(row[4])
            details_screen.ids.jdate.text =str(row[5])
            details_screen.ids.jdate.disabled = True
            details_screen.ids.desig.text = str(row[9])
            details_screen.ids.dept.text = str(row[8])
            details_screen.ids.gender.text = str(row[7])
            details_screen.ids.etype.text = str(row[6])


        mydb.commit()
        mydb.close()

    def update1(self,):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )

        c = mydb.cursor()
        details_screen = sm.get_screen('update')
        empid1 = details_screen.ids.empid.text
        full_name1 = details_screen.ids.full_name.text
        email_id1 = details_screen.ids.email_id.text
        phone_no1 = details_screen.ids.phone_no.text
        password1 = details_screen.ids.password.text
        jdate1 = details_screen.ids.jdate.text
        dept1 = details_screen.ids.dept.text
        desig1 = details_screen.ids.desig.text
        spinner_id11 = details_screen.ids.etype.text
        spinner_id21 = details_screen.ids.gender.text


        if spinner_id11 == "Admin":
            c.execute("UPDATE admin_records SET Name=%s,email_ID=%s,Phone_Number=%s,password=%s,Joining_Date=%s,Post=%s,Gender=%s,Department=%s,Designation=%s WHERE Employee_ID=%s",(full_name1,email_id1,phone_no1,password1,jdate1,spinner_id11,spinner_id21,dept1,desig1,empid1,))
            sm.current = 'login'
        elif spinner_id11 == "Teaching Employee":
            c.execute("UPDATE teaching_records SET Name=%s,email_ID=%s,Phone_Number=%s,password=%s,Joining_Date=%s,Post=%s,Gender=%s,Department=%s,Designation=%s WHERE Employee_ID=%s",(full_name1,email_id1,phone_no1,password1,jdate1,spinner_id11,spinner_id21,dept1,desig1,empid1,))
            sm.current = 'login'
        elif spinner_id11 == "Non-Teaching Employee":
            c.execute("UPDATE non_teaching_records SET Name=%s,email_ID=%s,Phone_Number=%s,password=%s,Joining_Date=%s,Post=%s,Gender=%s,Department=%s,Designation=%s WHERE Employee_ID=%s",(full_name1,email_id1,phone_no1,password1,jdate1,spinner_id11,spinner_id21,dept1,desig1,empid1,))
            sm.current = 'login'
        mydb.commit()









    def acreq(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        # create a cursor
        #ltype,name,fdate,tdate,reason,empid
        c = mydb.cursor()
        det = sm.get_screen('emp_leave_details')
        lt = det.ids.ltype.text
        emp=det.ids.empid.text
        nam=det.ids.name.text
        f=det.ids.fdate.text
        t=det.ids.tdate.text
        id=det.ids.empid.text
        r=det.ids.reason.text

        empt=det.ids.emp_type.text

        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")



        nf =f
        nt =t

        from_date_object = datetime.strptime(nf, "%Y-%m-%d")
        to_date_object = datetime.strptime(nt, "%Y-%m-%d")



        global l, n
        if empt == "Teaching Employee":
            l = "teaching_leave_record"

        elif empt == "Non-Teaching Employee":
            l = "non_teaching_leave_record"

        else:
            dialog = MDDialog(
                title='Warning',
                text=f"Select Employee type"
            )
            dialog.open()
        if lt == "Casual Leave":
            c.execute("SELECT Casual_Leave FROM leave_balance WHERE Employee_ID=%s", (emp,))
            row = c.fetchone()
            nv = row[0] - (to_date_object - from_date_object).days
            c.execute("UPDATE leave_balance SET Casual_Leave = %s WHERE Employee_ID=%s", (nv, emp,))
            c.execute("SELECT Sentence FROM notice WHERE Employee_ID = %s", (emp,))
            row = c.fetchone()

            if row is None:
                c.execute("INSERT INTO notice (Employee_ID, Sentence) VALUES (%s, 'Accepted')", (emp,))
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                mydb.commit()
                mydb.close()
            else:
                c.execute("UPDATE notice SET Sentence='Accepted' WHERE Employee_ID=%s", (emp,))
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                mydb.commit()
                mydb.close()
            sm.current = 'admin_dashboard'

        elif lt == "Earned Leave":
            c.execute("SELECT Earned_Leave FROM leave_balance WHERE Employee_ID=%s", (emp,))
            row = c.fetchone()
            nv = row[0] - (to_date_object - from_date_object).days
            c.execute("UPDATE leave_balance SET Earned_Leave = %s WHERE Employee_ID=%s", (nv, emp,))

            c.execute("SELECT Sentence FROM notice WHERE Employee_ID = %s", (emp,))
            row = c.fetchone()

            if row is None:
                c.execute("INSERT INTO notice (Employee_ID, Sentence) VALUES (%s, 'Accepted')", (emp,))
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                mydb.commit()
                mydb.close()
            else:
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date))
                c.execute("UPDATE notice SET Sentence='Accepted' WHERE Employee_ID=%s", (emp,))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                mydb.commit()
                mydb.close()
            sm.current = 'admin_dashboard'

        elif lt == "Child Care Leave":

            c.execute("SELECT Sentence FROM notice WHERE Employee_ID = %s", (emp,))
            row = c.fetchone()

            if row is None:
                c.execute("INSERT INTO notice (Employee_ID, Sentence) VALUES (%s, 'Accepted')", (emp,))
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                mydb.commit()
                mydb.close()
            else:
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date))
                c.execute("UPDATE notice SET Sentence='Accepted' WHERE Employee_ID=%s", (emp,))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                mydb.commit()
                mydb.close()
            sm.current = 'admin_dashboard'

        elif lt == "Maternity Leave":
            c.execute("SELECT Sentence FROM notice WHERE Employee_ID = %s", (emp,))
            row = c.fetchone()

            if row is None:
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date))
                c.execute("INSERT INTO notice (Employee_ID, Sentence) VALUES (%s, 'Accepted')", (emp,))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                mydb.commit()
                mydb.close()
            else:
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date))
                c.execute("UPDATE notice SET Sentence='Accepted' WHERE Employee_ID=%s", (emp,))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                mydb.commit()
                mydb.close()
            sm.current = 'admin_dashboard'

        elif lt == "Duty Leave":

            c.execute("SELECT Sentence FROM notice WHERE Employee_ID = %s", (emp,))
            row = c.fetchone()

            if row is None:
                c.execute("INSERT INTO notice (Employee_ID, Sentence) VALUES (%s, 'Accepted')", (emp,))
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                mydb.commit()
                mydb.close()
            else:
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date))
                c.execute("UPDATE notice SET Sentence='Accepted' WHERE Employee_ID=%s", (emp,))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                mydb.commit()
                mydb.close()
            sm.current = 'admin_dashboard'

        elif lt == "Special Leave":
            c.execute("SELECT Sentence FROM notice WHERE Employee_ID = %s", (emp,))
            row = c.fetchone()

            if row is None:
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date))
                c.execute("INSERT INTO notice (Employee_ID, Sentence) VALUES (%s, 'Accepted')", (emp,))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                mydb.commit()
                mydb.close()
            else:
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date))
                c.execute("UPDATE notice SET Sentence='Accepted' WHERE Employee_ID=%s", (emp,))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                mydb.commit()
                mydb.close()
            sm.current = 'admin_dashboard'

        elif lt == "Others":
            c.execute("SELECT Sentence FROM notice WHERE Employee_ID = %s", (emp,))
            row = c.fetchone()

            if row is None:
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date))
                c.execute("INSERT INTO notice (Employee_ID, Sentence) VALUES (%s, 'Accepted')", (emp,))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                mydb.commit()
                mydb.close()
            else:
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date))
                c.execute("UPDATE notice SET Sentence='Accepted' WHERE Employee_ID=%s", (emp,))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                mydb.commit()
                mydb.close()















    def rejreq(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()
        det = sm.get_screen('emp_leave_details')
        emp = det.ids.empid.text

        c.execute("SELECT Sentence FROM notice WHERE Employee_ID = %s", (emp,))
        row = c.fetchone()
        if row is None:
            c.execute("INSERT INTO notice (Employee_ID, Sentence) VALUES (%s, 'Rejected')", (emp,))
        else:
            c.execute("UPDATE notice SET Sentence='Rejected' WHERE Employee_ID=%s", (emp,))
            mydb.commit()
            sm.current = 'admin_dashboard'

        dete = sm.get_screen('emp_leave_details')
        global s, empid, t
        e = dete.ids.emp_type.text


        if e == "Teaching Employee":
            c.execute("DELETE FROM teaching_leave_record WHERE Employee_ID=%s",(emp,))
            sm.current='leave_list'

        elif e == "Non-Teaching Employee":
            c.execute("DELETE FROM non_teaching_leave_record WHERE Employee_ID=%s",(emp,))
            sm.current = 'leave_list'
        mydb.commit()
        mydb.close()









    def save_report(self,):
        layout = BoxLayout(orientation='vertical')

        with layout.canvas.before:
            Color(1, 1, 1, 1)  # Set canvas color
            self.rect = Rectangle(size=Window.size, pos=layout.pos)
        layout.bind(size=lambda *args: setattr(self.rect, 'size', args[1]))

        layout = self.root  # Assuming self.root is the root container for the layout hierarchy

        # Capture the layout as an image
        try:
            Window.screenshot(name='rep9.png')
            print("Screenshot saved successfully as 'rep9.png'.")
        except Exception as e:
            print(f"Error saving screenshot: {e}")

    def shownotice(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()
        details_screen = sm.get_screen('teaching_dashboard')
        empid = details_screen.ids.tea.text
        c.execute(f"select Sentence from notice where Employee_ID = %s",(empid,))
        row = c.fetchone()
        sm.current = 'notice'
        details_screen2 = sm.get_screen('notice')
        details_screen2.ids.noti.text=row[0]

    def check_login(self,email_phn,login_as,password):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        pas = password

        print(email_phn)


        dialog = MDDialog(
            title='Invalid',
            text='Wrong Login Details'
        )
        # create a cursor
        c = mydb.cursor()
        try:
            if login_as =="Admin":
                c.execute("SELECT * FROM Admin_Records WHERE email_ID = %s OR Phone_Number = %s",(email_phn,email_phn))
                row = c.fetchone()

                if row[4] == pas:
                    MDApp.get_running_app().root.current = 'admin_dashboard'
                    sm.current = 'admin_dashboard'
                    details_screen = sm.get_screen('admin_dashboard')
                    if details_screen:
                        details_screen.ids.admin.title = str(row[1])
                        details_screen.ids.admin.text = str(row[0])
                        self.show_dp()
                else:
                    dialog.open()

            if login_as =="Teaching Employee":
                c.execute("SELECT * FROM Teaching_records WHERE email_ID = %s OR Phone_Number = %s",(email_phn,email_phn))
                row = c.fetchone()
                print(row)
                if row[4] == pas:
                    MDApp.get_running_app().root.current = 'teaching_dashboard'
                    sm.current = 'teaching_dashboard'
                    details_screen = sm.get_screen('teaching_dashboard')
                    if details_screen:
                        details_screen.ids.tea.title = str(row[1])
                        details_screen.ids.tea.text = str(row[0])
                        self.show_dp()
                else:
                    dialog.open()



            if login_as =="Non-Teaching Employee":
                c.execute("SELECT * FROM Non_Teaching_Records WHERE email_ID = %s OR Phone_Number = %s",(email_phn,email_phn))
                row = c.fetchone()
                if row[4] == pas:
                    MDApp.get_running_app().root.current = 'non_teaching_dashboard'
                    sm.current = 'non_teaching_dashboard'
                    details_screen = sm.get_screen('non_teaching_dashboard')
                    if details_screen:
                        details_screen.ids.non_tea.title = str(row[1])
                        details_screen.ids.non_tea.text = str(row[0])
                        self.show_dp()
                else:
                    dialog.open()

        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Invalid login details "
            )
            dialog.open()




    def increment(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        tup = (0,)
        tap =0
        # create a cursor
        c = mydb.cursor()
        current_date = datetime.now().date()

        c.execute("SELECT Employee_ID FROM leave_balance")
        row = c.fetchall()
        for i in row:
            c.execute("SELECT last_updated from Leave_Balance WHERE Employee_ID = %s ", i)
            last_updated_date = c.fetchone()

            if (current_date - last_updated_date[0]).days >= 365:
                c.execute("UPDATE Leave_Balance SET Earned_Leave = Earned_Leave + 10 WHERE Employee_ID = %s", i)
                c.execute("UPDATE Leave_Balance SET Casual_Leave = 12 WHERE Employee_ID = %s", i)
                tup = i
                tap = str(tup[0])
                last_updated_date = current_date
                c.execute("UPDATE Leave_Balance SET last_updated = %s WHERE Employee_ID = %s",(last_updated_date,tap))
                mydb.commit()











    def signup(self,full_name,email_id,phone_no,password,jdate,spinner_id1,spinner_id2,spinner_id3,spinner_id4):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        global rand_num

        try:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            # create a cursor
            c = mydb.cursor()
            if (re.fullmatch(regex, email_id.text)):
                #insert_record
                #secondary table
                if spinner_id1.text=="Admin":
                    rand_n = random.randint(1, 100000)
                    rand_num = 'E' + str(rand_n) + 'A'

                elif spinner_id1.text=="Teaching Employee":
                    rand_n = random.randint(1, 100000)
                    rand_num = 'E' + str(rand_n) + 'T'
                elif spinner_id1.text=="Non-Teaching Employee":
                    rand_n = random.randint(1, 100000)
                    rand_num = 'E' + str(rand_n) + 'NT'
                else:
                    dialog = MDDialog(
                        title='Notice',
                        text="Select Employee Type "
                    )
                    dialog.open()


                c.execute(f"insert into secondary_table values('{rand_num}','{full_name.text}','{email_id.text}','{phone_no.text}','{password.text}','{jdate.text}','{spinner_id1.text}','{spinner_id2.text}','{spinner_id3.text}','{spinner_id4.text}')")
                dialog = MDDialog(
                    title='Notice',
                    text="You can login after the admin accepts "
                )
                dialog.open()

            else:
                dialog = MDDialog(
                    title='Notice',
                    text="Invalid Email "
                )
                dialog.open()

            mydb.commit()
            mydb.close()
        except Exception as e:
            dialog = MDDialog(
                title='Warning',
                text="Fill the form correctly "
            )
            dialog.open()


    #function for employee list
    def on_click_show_list(self):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()

        # Retrieve the employee data
        c.execute("SELECT Name, Employee_ID FROM secondary_table")
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
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()

        # Retrieve the employee details
        c.execute("SELECT * FROM secondary_table WHERE Employee_ID=%s", (item.secondary_text,))
        row = c.fetchone()
        sm.current = 'emp_detail'

        # Update the employee details screen with the retrieved data
        employee_details_screen = sm.get_screen('emp_detail')
        if employee_details_screen:

            employee_details_screen.ids.empid.text = str(row[0])
            employee_details_screen.ids.name.text = str(row[1])
            employee_details_screen.ids.email.text = str(row[2])
            employee_details_screen.ids.phone.text = str(row[3])
            employee_details_screen.ids.gender.text = str(row[7])
            employee_details_screen.ids.emp_type.text = str(row[6])
            employee_details_screen.ids.dept.text = str(row[8])
            employee_details_screen.ids.desig.text = str(row[9])

    ##function for employee list
    def on_click_show_list_of_all_employees(self):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()

        # Retrieve the employee data
        c.execute("SELECT Name, Employee_ID FROM teaching_records UNION SELECT Name, Employee_ID FROM non_teaching_records;")
        rows = c.fetchall()

        # Create the employee list
        employee_list = self.root.get_screen('emp_list').ids.container
        employee_list.clear_widgets()  # Clear existing widgets before populating the list
        for row in rows:
            # Create a TwoLineListItem with the employee name as text and phone number as secondary text
            item = TwoLineListItem(text=row[0], secondary_text=str(row[1]))
            # Bind the on_release event to the show_employee_details function
            item.bind(on_release=self.show_employee_details_of_employees)
            # Add the TwoLineListItem to the employee list
            employee_list.add_widget(item)


    ##function to show employee list on click
    def show_employee_details_of_employees(self, item):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()
        global row

        # Retrieve the employee details
        c.execute("SELECT * FROM teaching_records WHERE Employee_ID=%s", (item.secondary_text,))
        row = c.fetchone()
        if row is None:
            c.execute("SELECT * FROM non_teaching_records WHERE Employee_ID=%s", (item.secondary_text,))
            row = c.fetchone()


        sm.current = 'detail_employee'

        # Update the employee details screen with the retrieved data
        employee_details_screen = sm.get_screen('detail_employee')
        if employee_details_screen:

            employee_details_screen.ids.empid.text = str(row[0])
            employee_details_screen.ids.name.text = str(row[1])
            employee_details_screen.ids.email.text = str(row[2])
            employee_details_screen.ids.phone.text = str(row[3])
            employee_details_screen.ids.emp_type.text = str(row[6])
            employee_details_screen.ids.gender.text = str(row[7])
            employee_details_screen.ids.dept.text = str(row[8])
            employee_details_screen.ids.desig.text = str(row[9])




    #function to add employee(for admin section)
    def add_emp(self,empid,emp_type):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        print(emp_type)
        c = mydb.cursor()
        c.execute("SELECT * FROM secondary_table WHERE Employee_ID =%s ", (empid.text,))
        row = c.fetchone()
        if emp_type =="Teaching Employee":

            c.execute("INSERT INTO Teaching_records VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],))
            c.execute("INSERT INTO Leave_balance VALUES(%s,0,0,%s)", (row[0], row[5],))
            c.execute("DELETE FROM secondary_table WHERE Employee_ID=%s",(empid.text,))
            mydb.commit()
            mydb.close()


            MDApp.get_running_app().root.current = 'emp_list'

        elif emp_type =="Admin":
            print("a")
            c.execute("INSERT INTO Admin_Records VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],))
            c.execute("DELETE FROM secondary_table WHERE Employee_ID=%s",(empid.text,))
            mydb.commit()
            mydb.close()



            MDApp.get_running_app().root.current = 'emp_list'

        elif emp_type =="Non-Teaching Employee":

            c.execute("INSERT INTO Non_Teaching_Records VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],))

            c.execute("INSERT INTO Leave_balance VALUES(%s,0,0,%s)", (row[0], row[5],))
            c.execute("DELETE FROM secondary_table WHERE Employee_ID=%s", (empid.text,))
            mydb.commit()
            mydb.close()
            MDApp.get_running_app().root.current = 'emp_list'





    #function to remove employee(for admin section)
    def rem_emp(self,empid):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()

        c.execute("DELETE FROM secondary_table WHERE Employee_ID=%s",(empid.text,))

        MDApp.get_running_app().root.current = 'emp_list'

        mydb.commit()
        mydb.close()



    #function for employee list
    def on_click_teaching_leave_list(self):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()


        # Retrieve the employee data
        c.execute("SELECT Name, Empployee_ID FROM Teaching_leave_record")

        rows = c.fetchall()


        # Create the teaching employee leave list
        leave_list = self.root.get_screen('leave_list').ids.container
        leave_list.clear_widgets()  # Clear existing widgets before populating the list
        for row in rows:
            # Create a TwoLineListItem with the employee name as text and phone number as secondary text
            item = TwoLineListItem(text=row[0], secondary_text=str(row[1]))
            # Bind the on_release event to the show_employee_details function
            item.bind(on_release=self.show_employee_details)
            # Add the TwoLineListItem to the employee list
            leave_list.add_widget(item)

    #function for employee list
    def on_click_non_teaching_leave_list(self):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()


        # Retrieve the employee data
        c.execute("SELECT Name, Employee_ID FROM Non_Teaching_leave_record")

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

    def send_request(self, empid, name, leave_types, emp_type, fdate, tdate, reason):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        # create a cursor
        c = mydb.cursor()
        try:

            from_date = fdate
            to_date = tdate
            from_date_object = datetime.strptime(from_date, "%Y-%m-%d")
            to_date_object = datetime.strptime(to_date, "%Y-%m-%d")
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

            if leave_types == "Casual Leave":
                c.execute("SELECT Casual_Leave FROM leave_balance WHERE Employee_ID=%s", (empid,))
                row = c.fetchone()
                if (to_date_object - from_date_object).days > row[0]:
                    dialog = MDDialog(
                        title='Warning',
                        text=f"You have {row[0]} Casual Leaves"
                    )
                    dialog.open()
                else:
                    query = "INSERT INTO {} VALUES (%s,%s, %s, %s, %s, %s, %s)".format(l)
                    c.execute(query, (empid, name, leave_types, emp_type, fdate, tdate, reason))

                    self.goback()



            elif leave_types == "Earned Leave":
                c.execute("SELECT Earned_Leave FROM leave_balance WHERE Employee_ID=%s", (empid,))
                row = c.fetchone()
                if (to_date_object - from_date_object).days > row[0]:
                    dialog = MDDialog(
                        title='Warning',
                        text=f"You have {row[0]} Earned Leaves only"
                    )
                    dialog.open()
                else:
                    query = "INSERT INTO {} VALUES (%s,%s, %s, %s, %s, %s, %s)".format(l)
                    c.execute(query, (empid, name, leave_types, emp_type, fdate, tdate, reason))

                    self.goback()

            elif leave_types == "Child Care Leave":
                print(n)
                c.execute("SELECT Gender FROM {} WHERE Employee_ID = %s".format(n), (empid,))
                row = c.fetchone()
                if row[0] == "Male":
                    dialog = MDDialog(
                        title='Warning',
                        text=f"Only female employees can apply for CCL"
                    )
                    dialog.open()

                else:
                    query = "INSERT INTO {} VALUES (%s,%s, %s, %s, %s, %s, %s)".format(l)
                    c.execute(query, (empid, name, leave_types, emp_type, fdate, tdate, reason))

                    sm.current = 'certificate'





            elif leave_types == "Medical Leave":

                if emp_type == "Teaching Employee":
                    dialog = MDDialog(
                        title='Warning',
                        text=f"Only non-teaching employees can apply for Medical Leave"
                    )
                    dialog.open()

                else:
                    self.goback()

            elif leave_types == "Maternity Leave":
                c.execute("SELECT Gender FROM {} WHERE Employee_ID = %s".format(n), (empid,))
                row = c.fetchone()
                if row[0] == "Male":
                    dialog = MDDialog(
                        title='Warning',
                        text=f"Only female employees can apply for Maternity Leave"
                    )
                    dialog.open()
                else:
                    query = "INSERT INTO {} VALUES (%s,%s, %s, %s, %s, %s, %s)".format(l)
                    c.execute(query, (empid, name, leave_types, emp_type, fdate, tdate, reason))
                    self.goback()



            elif leave_types == "Duty Leave":
                query = "INSERT INTO {} VALUES (%s,%s, %s, %s, %s, %s, %s)".format(l)
                c.execute(query, (empid, name, leave_types, emp_type, fdate, tdate, reason))
                self.goback()

            elif leave_types == "Others":
                query = "INSERT INTO {} VALUES (%s,%s, %s, %s, %s, %s, %s)".format(l)
                c.execute(query, (empid, name, leave_types, emp_type, fdate, tdate, reason))
                dialog = MDDialog(
                    title='Notice',
                    text=f"Contact with the College"
                )
                dialog.open()

                self.goback()

            elif leave_types == "Special Leave":

                if (to_date_object - from_date_object).days > 547:
                    dialog = MDDialog(
                        title='Warning',
                        text=f"You can't take Special Leave more than 547 days or 18 months"
                    )
                    dialog.open()
                else:
                    query = "INSERT INTO {} VALUES (%s,%s, %s, %s, %s, %s, %s)".format(l)
                    c.execute(query, (empid, name, leave_types, emp_type, fdate, tdate, reason))

                    self.goback()

            mydb.commit()
            mydb.close()

        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Warning',
                text=f"Either you have a pending request or didn't fill the form correctly"
            )
            dialog.open()



    def callback_func(self):
        print("juj")






    def callback_for_menu_items(self,):
        print("ok")


    def no_function(self, instance):
        dialog = MDDialog(
            title='Warning',
            text=f"To apply for CCL, your child's age must be below 18 years old"
        )
        dialog.open()

    def goback(self):
        det = sm.get_screen('login')
        e = det.ids.login_as.text
        if e == "Teaching Employee":
            sm.current = 'teaching_dashboard'
        elif e == "Non-Teaching Employee":
            sm.current = 'non_teaching_dashboard'



    #function for employee list
    def on_click_teaching_leave_list(self):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()


        # Retrieve the employee data
        c.execute("SELECT Employee_ID, Name FROM Teaching_leave_record")

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
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()


        # Retrieve the employee data
        c.execute("SELECT Employee_ID, Name FROM Non_Teaching_leave_record")

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
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()

        # Retrieve the employee details
        c.execute("SELECT * FROM Non_Teaching_leave_record WHERE Employee_ID = %s", (item.secondary_text,))
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
        employee_details_screen.ids.empid.text = item.secondary_text



    def show_temployee_leave_details(self, item):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()

        # Retrieve the employee details
        c.execute("SELECT * FROM Teaching_leave_record WHERE Employee_ID = %s", (item.secondary_text,))
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
        employee_details_screen.ids.empid.text = item.secondary_text

    def employee_check_balance(self,):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        global detail,empid
        c = mydb.cursor()
        det = sm.get_screen('login')
        e = det.ids.login_as.text
        if e == "Teaching Employee":
            detail = sm.get_screen('teaching_dashboard')
            empid = detail.ids.tea.text

        elif e == "Non-Teaching Employee":
            detail = sm.get_screen('non_teaching_dashboard')
            empid = detail.ids.non_tea.text

        # Retrieve the employee details
        c.execute("SELECT Casual_Leave,Earned_Leave from Leave_Balance WHERE Employee_ID= %s", (empid,))
        row = c.fetchone()

        sm.current = 'check_balance'
        # Update the employee details screen with the retrieved data
        details_screen = sm.get_screen('check_balance')
        if details_screen:
            details_screen.ids.CL.text = str(row[0])
            details_screen.ids.EL.text = str(row[1])


    def update(self,empid,full_name,email_id,phone_no,password,jdate,spinner_id1,spinner_id2,spinner_id3,spinner_id4):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ahmex@123",
            database="test_db"
        )
        c = mydb.cursor()



LeavesystemApp().run()
