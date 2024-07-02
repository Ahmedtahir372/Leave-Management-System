from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivy.lang import Builder
from kivy.uix.image import AsyncImage
import mysql.connector

# MySQL Database Configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = '12345'
DB_NAME = 'test_db'

# KivyMD App
class ImageUploaderApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path
        )

    def build(self):
        return Builder.load_string('''
BoxLayout:
    orientation: 'vertical'

    MDTopAppBar:
        title: "Image Uploader"
        pos_hint:{"center_x":0.5,"center_y":0.8}

    MDCard:
        orientation: "vertical"
        size_hint: None, None
        size: "280dp", "180dp"
        pos_hint: {"center_x": .5}
        elevation: 10

        AsyncImage:
            id: image_preview
            source: ""

        MDRoundFlatButton:
            text: "Upload Image"
            pos_hint: {"center_x": .5}
            on_release: 
                app.file_manager.show("/")
''')

    def on_start(self):
        # Connect to MySQL Database
        self.conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        # Create a cursor object
        self.cursor = self.conn.cursor()

        # Load image from the database
        sql = "SELECT the_image FROM the_captured_image WHERE Employee_ID = 123"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()

        if result is not None:
            img_data = result[0]
            with open("image.jpg", 'wb') as image_file:
                image_file.write(img_data)

                self.root.ids.image_preview.source = "image.jpg"

    def select_path(self, path):
        # Update image preview
        self.root.ids.image_preview.source = path

        # Upload image to the database
        with open(path, 'rb') as image_file:
            img = image_file.read()

            sql = "UPDATE the_captured_image SET the_image = %s WHERE Employee_ID = 123"
            self.cursor.execute(sql, (img,))
            self.conn.commit()

        # Close the file manager
        self.exit_manager()

    def exit_manager(self, *args):
        self.file_manager.close()

    def on_stop(self):
        # Close the MySQL connection
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    ImageUploaderApp().run()
