from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
import smtplib
from kivymd.uix.dialog import MDDialog
import threading as th

class EmailApp(MDApp):
    def build(self):
        screen = Screen()

        # Create text fields for email details
        self.email_text = MDTextField(
            hint_text="Email",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            size_hint_x=None,
            width=300,
        )
        self.password_text = MDTextField(
            hint_text="Password",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            size_hint_x=None,
            width=300,

        )
        self.recipient_text = MDTextField(
            hint_text="Recipient Email",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint_x=None,
            width=300,
        )
        self.subject_text = MDTextField(
            hint_text="Subject",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            size_hint_x=None,
            width=300,
        )
        self.message_text = MDTextField(
            hint_text="Message",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            size_hint_x=None,
            width=300,
        )

        # Create button to send the email
        self.send_button = MDRectangleFlatButton(
            text="Send",
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            on_release=self.send_email,


        )

        screen.add_widget(self.email_text)
        screen.add_widget(self.password_text)
        screen.add_widget(self.recipient_text)
        screen.add_widget(self.subject_text)
        screen.add_widget(self.message_text)
        screen.add_widget(self.send_button)

        return screen

    def send_email(self, *args):
        try:
            # Get the email details from the text fields
            email = self.email_text.text
            password = self.password_text.text
            recipient = self.recipient_text.text
            subject = self.subject_text.text
            message = self.message_text.text

            print(email,password,recipient,subject,message)

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

            # Clear the text fields after sending the email
            self.email_text.text = ""
            self.password_text.text = ""
            self.recipient_text.text = ""
            self.subject_text.text = ""
            self.message_text.text = ""
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Warning',
                text=f"{e}"
            )
            dialog.open()
    def sendbythread(self,recipient,message):
        t1 = th.Thread(
            target = self.send_email,
            args = (recipient,message)
        )
        t1.start()

EmailApp().run()
