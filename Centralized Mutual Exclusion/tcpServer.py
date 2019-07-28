import socket
import sys
import time
import urllib.parse
import queue
import threading
# Starting the server
import tkinter.messagebox
username_client = ''
from _thread import *
from  tkinter import *
# root = Tk()
# root.mainloop()
q = queue.Queue()
lck = threading.Lock()
global MESSAGE
MESSAGE = ''
host = '127.0.0.1'
port = 6666

root = Tk()
newbox = tkinter.messagebox.showinfo("Servers message", "Connecting to server")
root.mainloop()


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # rec = tkinter.messagebox.showinfo("Server", "Connected to server")
    # print("Socket cre+ated...")
    # T.insert(INSERT, "Connecting to server")

    #print("Connecting to server")

except socket.error:
    # T.insert(INSERT, "Socket cannot be created ")
    print("Socket cannot be created ")
    sys.exit(0)

    # msgbox = tkinter.messagebox.showinfo("Message", reply)

    # starting and listening for the client

try:
    s.bind((host, port))
    # print("socket bound..")

except socket.error:
    sys.exit()

s.listen(100000)

def halt():
    lck.acquire()
    try:
        l = threading.enumerate()
        pop = q.get()
        time.sleep(pop)
        return True
    finally:
        lck.release()



def my_func(response, username, mytime):
    # print("Running")
    meth = halt()
    if (meth == True):
        #T.insert(INSERT, "Waiting for {} seconds for client {}\n".format(mytime, username))
        print("Waiting for {} seconds for client {}".format(mytime, username))
        response['message_one'] = " Server waited {} seconds for client {}\n".format(mytime, username)
        response['Content-Length'] = " " + str(len(response['message_one']))
        new_msg = urllib.parse.urlencode(response)
        MESSAGE = 'HTTP/1.1 POST' + " " + "Host: 127.0.0.1" + "User-Agent: Mozilla/5.0" + "Content-Type: charset=UTF-8" + " Sending the message" + "Date: " + time.asctime(time.localtime(time.time()))
        print(MESSAGE)
        #pollbox_server2 = tkinter.messagebox.showinfo("Server's Message", MESSAGE)
        con.send(new_msg.encode('utf-8'))



def client(con):
    # lck.acquire()
    response = {}
    while True:
        try:
            # multithreading for many clients
            # Upload the integer to the server
            # Creating the http message
            response['Host'] = ' 127.0.0.1'
            response['method'] = 'GET'
            response['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
            response['Content-Type'] = 'charset=UTF-8'
            response['message'] = "The number has been received "
            response['Content-Length'] = " " + str(len(response['message']))
            response['Date'] = " " + time.asctime(time.localtime(time.time()))
            MESSAGE = 'HTTP/1.1 GET' + " " + "Host: 127.0.0.1" + "User-Agent: Mozilla/5.0" + "Content-Type: charset=UTF-8" + " Requesting message from client" + "Date: " + time.asctime(time.localtime(time.time()))
            POST_MESSAGE = 'HTTP/1.1 POST' + " " + "Host: 127.0.0.1" + "User-Agent: Mozilla/5.0" + "Content-Type: charset=UTF-8" + " Requesting message from client" + "Date: " + time.asctime(time.localtime(time.time()))
            client_msg = urllib.parse.urlencode(response)
            print(POST_MESSAGE)
            con.send(client_msg.encode('utf-8'))
            #MESSAGE = 'HTTP/1.1 GET' + " " + "127.0.0.1" + " Mozilla/5.0" + " charset=UTF-8" + " Requesting message from client" + " " + time.asctime(time.localtime(time.time()))
            #box = tkinter.messagebox.showinfo("Server's Message", MESSAGE)
            print(MESSAGE)
            username_response = con.recv(1024).decode('utf-8')
            new_decode = urllib.parse.parse_qsl(username_response)
            d = dict(new_decode)
            myname = d['message']
            username_client = "CLIENT_" + myname
            reply = "Connected to " + username_client
            #tkinter.messagebox.showinfo("Client's Message", reply)
            # T.insert(INSERT, reply)
            #print(reply)
            print(reply)
            # del response['message']
            # with lck:
            print(MESSAGE)
            #poll1 = tkinter.messagebox.showinfo("Server's Message", MESSAGE)
            pool = con.recv(1024).decode('utf-8')
            resp = urllib.parse.parse_qsl(pool)
            # response = dict(resp)
            client_resp = dict(resp)
            mytime = int(client_resp['message'])
            q.put(mytime)
            my_func(response, username_client, mytime)




        except:
            errorbox = tkinter.messagebox.showinfo("Server's message", "Server disconnected")
            print("Server disconnected")
            sys.exit()
            s.close()









for k in range(3):
    con, addr = s.accept()
    thread = threading.Thread(target=client, args=(con, ))
    thread.start()

con.close()
s.close()




































'''
if __name__ == "__main__":
    def mine():
        

        


'''

































