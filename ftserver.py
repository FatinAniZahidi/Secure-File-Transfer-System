import sys
import tqdm
import os
import threading
import socket
import time

class Server:

     #create socket (TCP Protocol)
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.accept_connections()


    def accept_connections(self):
        ip = str(input('\tEnter Server Ip Address : '))
        port = int(input('\tEnter Desired Port Number : '))

        self.sock.bind((ip,port))  #associate the socket with specific ip address and port number
        self.sock.listen(100)  #server listen for incoming connection
        print('\n')

        while 1:
            c, addr = self.sock.accept()   #accept connection rqest from the  client
            print('\t------------------------------------------')
            print('\tSuccessfully Connected to :' + addr[0])  #print client ip address
            print('\t------------------------------------------')

            #create thread
            threading.Thread(target=self.handle_client,args=(c,addr,)).start()

    def handle_client(self,c,addr):
        data = c.recv(1024).decode()
    
        if not os.path.exists(data):
            c.send("file-doesn't-exist".encode())

        else:
            c.send("file-exists".encode())
            print('Sending',data)
            if data != '':
                file = open(data,'rb')
                data = file.read(1024)
                while data:
                    c.send(data)
                    data = file.read(1024)

                c.shutdown(socket.SHUT_RDWR)
                c.close()
                

server = Server()

