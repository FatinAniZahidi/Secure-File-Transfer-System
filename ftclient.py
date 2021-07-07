import socket
import os

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        self.target_ip = input('Enter ip --> ')
        self.target_port = input('Enter port --> ')

        self.s.connect((self.target_ip,int(self.target_port)))

        self.main()

    def reconnect(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((self.target_ip,int(self.target_port)))

def main(self):
        #verify a new user
        New = input('\t\nWhich user are you? [ y - new user | n - existing user] :')
        self.sock.send(New.encode())   #send input user to server
        if New == 'y':   #if new user
            username = input('\tEnter New Username : ')
            self.sock.send(username.encode())

            password = getpass.getpass('\tEnter New Password : ', stream=None)
            self.sock.send(password.encode())

            #register new user
            register = self.sock.recv(1024)

            if register.decode() == "continue":
                print('\t\t\nPlease Re-enter Your Credential')

                #login new registered user
                username = input('\tEnter Username : ')
                self.sock.send(username.encode())

                password = getpass.getpass('\tEnter Password : ', stream=None)
                self.sock.send(password.encode())

                #if the username and password does not exist in the login.txt
                login = self.sock.recv(1024)
                if login.decode() == "Not-a-user":
                    print("\tYour Credential Could Not Be Verified ! Connection will be terminate !")

                    self.sock.shutdown(socket.SHUT_RDWR)
                    self.sock.close()
                    sys.exit()
                else:
                    print(login.decode())  #print welcome new user

    def main(self):
        while 1:
            file_name = input('Enter file name on server --> ')
            self.s.send(file_name.encode())

            confirmation = self.s.recv(1024)
            if confirmation.decode() == "file-doesn't-exist":
                print("File doesn't exist on server.")

                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close()
                self.reconnect()

            else:        
                write_name = 'from_server '+file_name
                if os.path.exists(write_name): os.remove(write_name)

                with open(write_name,'wb') as file:
                    while 1:
                        data = self.s.recv(1024)

                        if not data:
                            break

                        file.write(data)

                print(file_name,'successfully downloaded.')

                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close()
                self.reconnect()
                
client = Client()
