from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import BaseSnackbar


class CustomSnackbar(BaseSnackbar):
    text = StringProperty(None)
    icon = StringProperty(None)
    font_size = NumericProperty("15sp")


class Test(MDApp):
    def build(self):
        return

    def on_start(self):
        def temp():
            '''i wan to upgrate the label'''
        self.player_count = self.add_widget(MDLabel(
            text = self.player_choise+'/'+str(self.player_velu)
            )
        )
        MDFlatButton(text='upg', on_press=temp)

Test().run()