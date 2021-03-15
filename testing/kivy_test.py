#!/usr/bin/python3

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.label import MDLabel

class MyApp(MDApp):

    def build(self):
        screen = Screen()

        label = MDLabel(text='Hello', theme_text_color='Error', font_style='H1', halign='center')

        button = MDFloatingActionButton(icon='android', pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                        size_hint=(0.2, 0.25))
        screen.add_widget(button)
        screen.add_widget(label)
        return screen

MyApp().run()