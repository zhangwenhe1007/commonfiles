#!/usr/bin/python3

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import num_helper, sms_helper

import socket
HEADER = 1024
PORT = 9001
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"
SERVER = "192.168.1.19"
ADDR = (SERVER, PORT)


class Alerte_Anti_Arnaqueurs(MDApp):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    def build(self):

        self.theme_cls.primary_palette = 'Green'
        screen = Screen()
        btn_num = MDRectangleFlatButton(text='Enter', pos_hint={'center_x': 0.5, 'center_y': 0.65},
                                        on_release=self.get_data_num)
        screen.add_widget(btn_num)

        self.num = Builder.load_string(num_helper)
        screen.add_widget(self.num)
        return screen

    def get_data_num(self, obj):

        if self.num.text == "":
            self.response = "Please enter a number"
        else:
            self.send(obj=(self.num.text + '1'))

        close1_btn = MDFlatButton(text='Close', on_release=self.close_dialog)
        self.dialog = MDDialog(title='Verification', text=self.response, size_hint = (0.7, 1), buttons = [close1_btn])
        self.dialog.open()

    def send(self, obj):
        message = obj.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - (len(send_length)))

        self.client.send(send_length)
        self.client.send(message)
        self.response = self.client.recv(HEADER).decode(FORMAT)
        return self.response

    def close_dialog(self, obj):
        self.dialog.dismiss()

Alerte_Anti_Arnaqueurs().run()