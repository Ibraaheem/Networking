import ssl
import base64
from socket import *
from getpass import getpass

def main():

    endmsg = b"\r\n.\r\n"

    mailServer = 'smtp.gmail.com'                                   
    clientSocket = socket(AF_INET, SOCK_STREAM)                        
    clientSocket.connect((mailServer, 25))                              
    recv=clientSocket.recv(1024)                                        
    print(recv)                                                          
    if '220' not in str(recv):
        print('220 NOT RECEIVED.')                     

    heloCommand = b'EHLO Test\r\n'
    clientSocket.send(heloCommand)                                      
    recv1=clientSocket.recv(1024)                                       
    print(recv1)                                                         
    if '250' not in str(recv1):                                               
        print('250 NOT RECEIVED.')

    tlsCommand = b'STARTTLS \r\n'
    clientSocket.send(tlsCommand)
    recv1 = clientSocket.recv(1024)
    print(recv1)
 
    clientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_TLSv1)

    username = input('USERNAME: ')
    password = getpass('PASSWORD: ')
    
    base64_str = ("\x00"+username+"\x00"+password).encode()
    base64_str = base64.b64encode(base64_str)
    authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
    clientSocket.send(authMsg)
    recv_auth = clientSocket.recv(1024)
    print(recv_auth.decode())

    recipient = input('TO: ')
    imsg = input("MESSAGE: ")
    msg = "\r\n "+imsg+""
    mailFrom = "MAIL FROM:<"+username+">\r\n"
    clientSocket.send(mailFrom.encode())
    recv1 = clientSocket.recv(1024)
    print(recv1.decode())

    recipient = "RCPT TO: <"+recipient+">\r\n"
    clientSocket.send(recipient.encode())
    recv1 = clientSocket.recv(1024)
    if '250' not in str(recv1.decode()):                                               
        print('250 NOT RECEIVED.')

    clientSocket.send(b'DATA\r\n')                                       
    recv1 = clientSocket.recv(1024)                                   
    print(recv1)                                                         
    if '354' not in str(recv1):                                            
        print('250 NOT RECEIVED.')                   

    clientSocket.send(msg.encode())
    clientSocket.send(endmsg)
    recv_msg = clientSocket.recv(1024)
    print(recv_msg)

    quit = b"QUIT\r\n"
    clientSocket.send(quit)
    recv1 = clientSocket.recv(1024)
    print(recv1)
    clientSocket.close()

if __name__ == '__main__':
    main()
