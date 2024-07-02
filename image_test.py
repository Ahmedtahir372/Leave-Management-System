from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivy.lang import Builder
import mysql.connector
from kivy.uix.screenmanager import ScreenManager




class MyApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path,
        )
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        global sm

        sm = ScreenManager()
        sm.add_widget(Builder.load_file("upload_certificate.kv"))
        return sm

    def open_file_manager(self):
        self.file_manager.show('/')  # Show the file manager starting from the root directory

    def select_path(self, path):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        self.cursor = self.mydb.cursor()
        # Handle the selected image file path here
        self.file_manager.close()
        print("Selected File:", path)
        det = sm.get_screen('certificate')
        det.ids.my_image.source = path
        with open(path, 'rb') as image_file:
            img = image_file.read()

            sql = "UPDATE the_captured_image SET the_image = %s WHERE Employee_ID = 123"
            self.cursor.execute(sql, (img,))
            self.mydb.commit()



    def exit_file_manager(self, *args):
        self.file_manager.close()




MyApp().run()
