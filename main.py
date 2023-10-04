from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.dialog import MDDialog
import random
from kivy.properties import ObjectProperty

Builder.load_file('style.kv')

class Style(MDAnchorLayout):
    themes='Light'
    image_top_meno=ObjectProperty()
    
    def about(self):
        d=MDDialog(title='About',
                   text='This application building with <<< AliasgharZahdyan >>>')
        d.open()

    def change_theme(self):
        self.theme_cls.theme_style=self.themes
        if self.themes=='Light':
            self.themes='Dark'
        else:
            self.themes='Light'

    def change_color_top_meno(self):
        color_primaty=['Red','Pink','Purple','DeepPurple',
    'Indigo','Blue','LightBlue','Cyan','Teal','Green',
    'LightGreen','Lime','Yellow','Amber','Orange', 'DeepOrange',
    'Brown','Gray', 'BlueGray']
        self.theme_cls.primary_palette=random.choice(color_primaty)
        self.theme_cls.primary_hue='900'

    def change_image_top_meno(self):
        image_name=['0.jpg','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg',
                    '6.jpg','7.jpg','8.jpg','9.jpg']
        self.image_top_meno.source=random.choice(image_name)

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style='Dark'
        return Style()
    

MainApp().run()

