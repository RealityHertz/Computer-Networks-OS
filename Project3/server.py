#Jaxson Billings
#jlbillings42
#CSC 4200 Project 2
#March 22, 2023

#Imports
import logging
import socket
import random
import sys

#Initialization
log = sys.argv[4]
logging.Config(filename=log, format='%(filename)s: %(message)s', level=logging.DEBUG)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = sys.argv[2]
port = int(port)
s.bind((host, port))

#Output
print("hostname = ",host)
print("port = ",port)

#While Loop
s.listen(5)
while True:
    client, address = s.accept()
    print('Connected Address: ', address)
    client.send(bytes('Connected'))
    recvData = client.recv(10000000).decode()
    print("client: ", recvData)

    #IF Statement to Open File
    if(recvData == "network" or recvData == "NETWORK"):
       q = open('quotes.txt')
       quote = q.readlines()
       line_count = 0
       for line in quote:
           if line != "\n":
               line_count +=1

       #Random Generator
       n = random.randint(0,line_count-1)
       Quote = quote[n]

       #Print Statements
       print("line: ",n)
       print(Quote)
       client.send(sendQuote.encode('utf-8'))
       q.close
   #Close/End
   client.close()                          
   logging.debug (address) 
