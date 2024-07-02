from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector
from io import BytesIO
from PIL import Image
from kivy.uix.image import Image as CoreImage

Builder.load_string('''
<ImageChooserScreen>:
    BoxLayout:
        orientation: 'vertical'
        AsyncImage:
            id: my_image
            source: ''
''')

class ImageChooserScreen(Screen):
    pass

class ImageChooserApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        sm = ScreenManager()
        sm.add_widget(ImageChooserScreen(name='img_test'))
        return sm

    def on_start(self):
        self.now_view()

    def now_view(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()
        c.execute("SELECT the_image FROM the_captured_image WHERE Employee_ID = 123")
        row = c.fetchone()
        if row:
            image_data = row[0]
            image = Image.open(BytesIO(image_data))
            image.save("temp_image.jpg")
            sm = self.root
            det = sm.get_screen('img_test')
            det.ids.my_image.source = 'temp_image.jpg'

ImageChooserApp().run()
