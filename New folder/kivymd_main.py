#!/usr/bin/python3

#main program to run KivyMD

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDFloatingActionButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import num_helper, sms_helper
from wave_test import listen
import speech_recognition as sr

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
        #Build root widget, that is the core application or interface
        self.theme_cls.primary_palette = 'Green'
        screen = Screen()
        #Create a screen variable and add elements to the Screen to display them
        btn_num = MDRectangleFlatButton(text='Enter', pos_hint={'center_x': 0.5, 'center_y': 0.65},
                                        on_release=self.get_data_num)
        screen.add_widget(btn_num)
        btn_sms = MDRectangleFlatButton(text='Enter', pos_hint={'center_x': 0.5, 'center_y': 0.45},
                                        on_release=self.get_data_sms)
        screen.add_widget(btn_sms)
        icon_record = MDFloatingActionButton(icon='microphone',
                                             pos_hint={'center_x': 0.5, 'center_y': 0.25},
                                             size_hint_x=None,
                                             on_press=self.get_voice,
                                             on_release=self.show_voice)

        screen.add_widget(icon_record)

        self.num = Builder.load_string(num_helper)
        screen.add_widget(self.num)

        self.sms = Builder.load_string(sms_helper)
        screen.add_widget(self.sms)

        return screen

#functions that activate on button release/ on button press

    def get_data_num(self, obj):

        if self.num.text == "":
            self.response = "Please enter a number"
        else:
            self.send(obj=(self.num.text + '1'))

        close1_btn = MDFlatButton(text='Close', on_release=self.close_dialog)
        self.dialog = MDDialog(title='Verification', text=self.response, size_hint=(0.7, 1), buttons=[close1_btn])

        self.dialog.open()

    def get_data_sms(self, obj):
        if self.sms.text == "":
            check_string = "Please enter the message"
            close_btn = MDFlatButton(text='Close', on_release=self.close_dialog)
            self.dialog = MDDialog(title='Verification',
                                   text=check_string,
                                   size_hint=(0.7, 1),
                                   buttons=[close_btn])
        else:
            self.send(obj=(self.sms.text + '2'))
            self.verdict = self.client.recv(HEADER).decode(FORMAT)

            self.list = self.response.split('-')
            self.showit = str(self.list[0]) + '\n' + str(self.list[1])

            print(self.response, 'next', self.verdict)

            close_btn = MDFlatButton(text='Close', on_release=self.close_dialog)
            yes_btn = MDRaisedButton(text='Yes', on_release=self.yes)
            no_btn = MDRaisedButton(text='No', on_release=self.no)
            self.dialog = MDDialog(title='Verification', text=self.showit+'\n'+ 'Was the message correctly interpreted?',
                                   size_hint=(0.7, 1),
                                   buttons=[close_btn,yes_btn,no_btn])
        self.dialog.open()

    def yes(self, obj):
        self.send(obj=(self.verdict + 'a'))
        self.send(obj=(self.sms.text))
        self.dialog.dismiss()

    def no(self, obj):
        self.send(obj=(self.verdict + 'u'))
        self.send(obj=(self.sms.text))
        self.dialog.dismiss()

    def get_voice(self, obj):
#On press of icon button: activate microphone and record

        print(listen())
        recognizer = sr.Recognizer()
        listened = sr.AudioFile('listened.wav')

        with listened as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            self.recorded = recognizer.recognize_google(audio)

        except sr.UnknownValueError:
            self.recorded = ("Oops! Didn't catch that")

        except sr.RequestError as e:
            self.recorded = ("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

        print(self.recorded)

    def show_voice(self, obj):

#On release of icon button: finish recording voice and analyze with Bayes

        self.send(obj=(self.recorded + '4'))
        self.list = self.response.split('-')
        self.showit = str(self.list[0]) + '\n' + str(self.list[1])

        check_string = "Your message was:\n" + self.recorded + '\n\n' + self.showit

        close_btn = MDFlatButton(text='Close', on_release=self.close_dialog)

        self.dialog = MDDialog(title='Verification', text=check_string,
                               size_hint=(0.7, 1),
                               buttons=[close_btn])
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
