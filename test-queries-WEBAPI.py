import time
import socket
import re
#import encode
#import decode


HOST = '127.0.0.1'
PORT = 12345 #MT4
#HOST = '192.168.56.101'
#PORT = 443  #MT5

hello = print('\nQuery Script v0.01\n ')
answer = ""
while answer == "":   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.connect((HOST, PORT))
    apiquery = input('Input your query. Example: "getallbalances" \n$: ')
    action = ('action=')

    s.connect((HOST, PORT))
    s.send(action.encode()+apiquery.encode())
    #print(s.recv(1024))
    received = s.recv(1024)

    received = True

    while received:
        received = s.recv(1024)
        print(received)
    
    s.close()
    answer = ''
