'''
Name : Anirudh Deshpande
NetID: axr8193
'''


import socket
import sys
import random
import tkinter.messagebox
from tkinter import *
import urllib.parse
from time import *

root = Tk()
newbox = tkinter.messagebox.showinfo("Client connection", "Connecting to client")
root.mainloop()

def send_username(username_resp, i):
    username_resp['Host'] = ' 127.0.0.1'
    username_resp['method'] = 'POST'
    username_resp['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    username_resp['Content-Type'] = 'charset=UTF-8'
    username_resp['message'] = str(i)
    username_resp['Content-Length'] = " " + str(len(username_resp['message']))
    username_resp['Date'] = " " + asctime(localtime(time()))
    client_msg = urllib.parse.urlencode(username_resp)
    HTTP_MESSAGE = 'HTTP/1.1 POST' + " " + "127.0.0.1" + " Mozilla/5.0" + " charset=UTF-8" + " Sending the message" + " " + asctime(localtime(time()))
    print(HTTP_MESSAGE)
    #pollbox_server1 = tkinter.messagebox.showinfo("Client's Message", HTTP_MESSAGE)
    s.send(client_msg.encode('utf-8'))

def send_time(client_response):
    time_to_wait = random.randint(3, 11)
    client_response['Host'] = ' 127.0.0.1'
    client_response['method'] = 'POST'
    client_response [       'User-Agent'] = 'Mozilla/5.0'
    client_response['Content-Type'] = 'charset=UTF-8'
    client_response['message'] = str(time_to_wait)
    client_response['Content-Length'] = " " + str(len(client_response['message']))
    client_response['Date'] = " " + asctime(localtime(time()))
    msg_client = urllib.parse.urlencode(client_response)
    HTTP_MESSAGE = 'HTTP/1.1 POST' + " " + "Host: 127.0.0.1" + "User-Agent: Mozilla/5.0" + "Content-type: charset=UTF-8" + " Sending the message" + "Date: " + asctime(localtime(time()))
    print(HTTP_MESSAGE)
    #pollbox_server2 = tkinter.messagebox.showinfo("Client's Message", HTTP_MESSAGE)
    s.send(msg_client.encode('utf-8'))
    sleep(time_to_wait)



def main():
    host = 'localhost'
    ip = socket.gethostbyname(host)
    port = 6666
    i = 0
    # count = 1
    HTTP_MESSAGE = ''
    username_resp = {}
    client_response = {}

    try:
        s.connect((ip, port))
        #T.insert(INSERT, "Connection made...")
        print("Connection made...")



    except socket.error:
        print("Host cannot be connected..")
        sys.exit()

    while True:
        try:
            i = i + 1
            # time.sleep(time_to_wait)
            HTTP_MESSAGE = 'HTTP/1.1 GET' + " " + "Host: 127.0.0.1" + "User-Agent: Mozilla/5.0" + "Content-Type: charset=UTF-8" + " Polling the server message" + "Date: " + asctime(localtime(time()))
            print(HTTP_MESSAGE)
            #pollbox1 = tkinter.messagebox.showinfo("Client's Message", HTTP_MESSAGE)
            m = s.recv(1024).decode('utf-8')
            # parsing the http message
            resp = urllib.parse.parse_qsl(m)
            response = dict(resp)
            # parsing the response and printing on the GUI
            # T.insert(INSERT, response['message'] + "\n")
            msgbox = tkinter.messagebox.showinfo("Server's Message", response['message'])
            print(response['message'])
            send_username(username_resp, i)
            send_time(client_response)
            # print(m)
            HTTP_MESSAGE = 'HTTP/1.1 GET' + " " + "Host: 127.0.0.1" + "User-Agent: Mozilla/5.0" + "Content-Type: charset=UTF-8" + " Polling the server message" + "Date: " + asctime(localtime(time()))
            print(HTTP_MESSAGE)
            #pollbox2 = tkinter.messagebox.showinfo("Client's Message", HTTP_MESSAGE)
            new_msg = s.recv(1024).decode('utf-8')
            res = urllib.parse.parse_qsl(new_msg)
            d = dict(res)
            # T.insert(INSERT, response['message_one'] + "\n")
            box = tkinter.messagebox.showinfo("client Message", d['message_one'])
            print(d['message_one'])




        except:
            discon = tkinter.messagebox.showinfo("Client connection", "client has disconnected")
            #print("client has disconnected")
            sys.exit()






    #root.mainloop()




try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print("Socket created ..")

except socket.error:
    pass
    #print("Cannot create the socket...")





main()








