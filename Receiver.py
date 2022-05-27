import utils as ut
import socket
import json
import receiverClass as rc

#--------------------------------------------------------------
# initialize the socket 
# URL : https://www.geeksforgeeks.org/socket-programming-python/
#--------------------------------------------------------------
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 7634
s.bind((host,port))
s.listen(5)
con,addr = s.accept()
print("got connection from ",addr)

#--------------------------------------------------------------
# initialize instance from the receiver class
#--------------------------------------------------------------
receiver= rc.receiver()

#--------------------------------------------------------------
# Read the values of P , Q from a file or generate them randomly
#--------------------------------------------------------------
p = 0
q = 0
choice = int(input("\n(1) keys with specific bit size  \n(2) enter your  p, q \nChoice: "))
if (choice == 1):
    size = int (input("Enter the key size(bits): "))    
    p,q = ut.generate_primes_bits(size)

if (choice == 2):
    p = int(input("\nEnter p : "))
    if(not ut.prime(p)):
        while(not (ut.prime(p))):
            p = int(input("\n Enter p , should be prime and != p : "))
        
    else:
        q = int(input("\n Enter q : "))
        while(not (ut.prime(q)) or p==q ):
            q = int(input("\n Enter q , should be prime and != p : "))


else:
    p = 2475730193
    q = 908416969

#--------------------------------------------------------------
# generate the public key of the reciever
#--------------------------------------------------------------
 
e= ut.generate_e( p , q)
print("e",e)
#--------------------------------------------------------------
# send the public key of the reciever
#--------------------------------------------------------------

receiver.p=p
receiver.q=q
receiver.e=e
receiver.n=p*q
public_key=[e , p*q]

keys_list = json.dumps(public_key)
con.send(keys_list.encode())

while True:
    # try:
        C = con.recv(1024)
        Cipher = C.decode()
        print('\n')
        print("cipher text received:",Cipher)
        decrypted = receiver.decrypt(Cipher)
        print('\n')
        with open('outputs.txt', 'a') as f:
            f.write("original msg after decryption : " + decrypted + "\n")
        f.close()
    # except:
    #     con.close()
        

        
     
      