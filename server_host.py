#import socket module
from socket import *
import time, threading
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.bind(('', 6789))
serverSocket.listen(1)
#Fill in end
while True:
        
        #Establish the connection
        print('Ready to serve...')
        #Fill in start
        
        #Fill in end
        try:
                connectionSocket, addr = serverSocket.accept()
                message = connectionSocket.recv(1024) #Fill in start #Fill in end
                print((message.split()[1])[1:])
                filename = message.split()[1][1:]
                f = open(filename,"r")
                outputdata = f.read() #Fill in start #Fill in end
                f.close()
                #Send one HTTP header line into socket
                #Fill in start
                content= ("HTTP/1.1 200 OK\r\n" +  \
                                                "Content-Length: %d\r\n" % len(outputdata) +  \
                                                "Date: %s \r\n" %  time.strftime('%Y-%m-%d', time.localtime(time.time() ) )  +  \
                                                "Content-Type: text/html;charset=utf-8\r\n\r\n" +  \
                                                outputdata)
                print(content)
                connectionSocket.send(content.encode())
                
                #Fill in end
                #Send the content of the requested file to the client
                connectionSocket.close()
        except IOError:
                #Send response message for file not found
                #Fill in start
                connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())
                #Fill in end
                #Close client socket
                #Fill in start
                connectionSocket.close()
               
serverSocket.close()    
sys.exit()#Terminate the program after sending the corresponding data