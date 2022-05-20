import socket
import json
import senderClass as sc
#--------------------------------------------------------------
# initialize the socket 
#--------------------------------------------------------------
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=7634  
s.connect((host,port))

#--------------------------------------------------------------
# initialize instance from the sender class
#--------------------------------------------------------------
sender = sc.sender() 

#--------------------------------------------------------------------
# Start the communication by receiving the public key from the sender
#--------------------------------------------------------------------

keys = s.recv(1024).decode()
keys = json.loads(keys)
e = keys[0]
n = keys[1]
    
#--------------------------------------------------------------
#     sending ....
#--------------------------------------------------------------
# print("e",e)
# print("n",n)
sender.e = e
sender.n = n  

while True:
    # try:
        M = input("type the message to be sent : > ")
        cipher_text= sender.encrypt(M)   
        print("cipher sent : ",cipher_text) 
        s.send(cipher_text.encode())   
        
        with open('inputs.txt', 'a') as f:
            f.write("message : " + M + "\n")
        f.close() 
    # except:
    #     s.close() 
