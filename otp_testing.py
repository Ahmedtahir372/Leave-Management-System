from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
import random
Window.size = (310,570)
class LeaveApp(MDApp):
    def build(self):

        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("new_signup2.kv"))
        return sm

    def verify_otp(self):
        rand = str(random.randint(100000, 999999))
        print(rand)

        dialo = MDDialog(
            title="Enter the OTP sent to you",
            type="custom",
            content_cls=MDTextField(hint_text="Enter OTP", size_hint=(None, None), width=280),
            buttons=[
                MDFlatButton(text="Cancel", on_release=lambda *args: dialo.dismiss()),
                MDFlatButton(text="OK", on_release=lambda *args: self.process_input(rand,dialo.content_cls.text,dialo)),
            ],
        )
        dialo.open()


    def process_input(self, rand,otp,dialo):
        print (rand,otp)
        try:
            if otp == rand:
                print("continue")
                dialog = MDDialog(
                    title='Notice',
                    text="Your emeail is verified"
                )
                dialog.open()
                #close another dialog from here
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







LeaveApp().run()