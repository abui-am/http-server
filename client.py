from socket import *
import sys
import logging

clientsocket = socket(AF_INET, SOCK_STREAM)

if len(sys.argv) != 4:
    print(len(sys.argv))
    print("Your command is not right. Please be in this format:client.py server_host server_port filename")
    sys.exit(0)

host = str(sys.argv[1])
port = int(sys.argv[2])
request = str(sys.argv[3])
request = "GET /" + request + " HTTP/1.1"
try:
    clientsocket.connect((host,port))
except Exception:
    # print exception cause
    logging.exception("An exception was thrown!")
    print ("Please try again.\r\n")
    sys.exit(0)
clientsocket.send(request.encode())
    
response = clientsocket.recv(1024)
print(response.decode())
clientsocket.close()


 