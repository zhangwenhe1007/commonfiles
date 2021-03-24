#!/usr/bin/python3

#START THE SERVER BEFORE OPENING APPLICATION

import socket
import threading
from call_location import call_location
from sms_testing_old import message_rating
from spam_update import spam_update 
from spam_update import add_message

HEADER = 1024
PORT = 9001
SERVER = socket.gethostbyname(socket.gethostname()) #0.0.0.0
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'New connection {addr} connected.')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg[-1] == '1':
                print('Received the number')
                num = msg[:-1]
                response = call_location(num)
                print('The number is: '+num+'\n'+response)

            if msg[-1] == '2':
                print('Received the message')
                sms = msg[:-1]
                outputs = message_rating(sms)
                conn.send((outputs[0]).encode(FORMAT))
                response = outputs[1]
                print('The message is: '+sms)

            if msg[-1] == 'a':
                print('Received rating correction')
                rating = msg[:-1]
                conn.send('Received'.encode(FORMAT))
                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length:
                    msg_length = int(msg_length)
                    sms = conn.recv(msg_length).decode(FORMAT)
                    print('Your message was:'+sms+'\n'+'This message is '+rating)
                    add_message(sms,[rating])
                    conn.send('Received'.encode(FORMAT))

            if msg[-1] == 'u':
                print('Received rating correction')
                rating = msg[:-1]
                conn.send('Received'.encode(FORMAT))
                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length:
                    msg_length = int(msg_length)
                    sms = conn.recv(msg_length).decode(FORMAT)
                    print('Your message was:'+sms+'\n'+'This message is not '+rating)
                    spam_update(sms, [rating])
                    conn.send('Received'.encode(FORMAT))

            if msg[-1] == '4':
                print('Received the audio')
                sms = msg[:-1]
                outputs = message_rating(sms)
                response = outputs[0]
                print('The message is: '+sms)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            conn.send(response.encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print(f'Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active connections {threading.activeCount() - 1}")

print("STARTING")
start()