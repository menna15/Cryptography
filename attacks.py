import utils as ut
import receiverClass as rc
import senderClass as sc
import math
# ---------------------------------------
#     chosen cipher attack
#----------------------------------------
def CCA(C,e,n):
    r = ut.generate_r(n) 
    C_dash= C * ut.PowMod(r,e,n)
    Y = ut.str2int(bob.decrypt(ut.int2str(C_dash)))
    M = ut.PowMod(Y * (ut.InvertModulo(r,n)),1,n)
    print(ut.int2str(M))
    return(ut.int2str(M))

# ---------------------------------------
#     mathematical attack
#----------------------------------------
def mathematical_attack(cipher, e, n):
    deciphered = ''
    for p in range(2, int(math.sqrt(n)+1)):
        if(n % p == 0):
            print(p)
            bob.q = n//p
            bob.e = e
            print(bob.e)
            bob.p = p
            bob.n = n
            deciphered = bob.decrypt(cipher)
            print(deciphered)
    return deciphered

if __name__ == __name__:
    # ---------------------------------------
    #     Initialize sender and reciever
    #----------------------------------------
    bob = rc.receiver()

    alice = sc.sender()

    # read p and q values
    p = 0
    q = 0
    choice = int(input("\n(1) keys with specific bit size  \n(2) enter your  p, q \nChoice: "))
    if (choice == 1):
        size = int (input("Enter the key size(bits): "))    
        p,q = ut.generate_primes_bits(size)

    if (choice == 2):
        p = int(input("\nEnter p : "))
        if(not ut.ISprime(p)):
            while(not (ut.ISprime(p))):
                p = int(input("\n Enter p , should be prime and != p : "))
            
        else:
            q = int(input("\n Enter q : "))
            while(not (ut.ISprime(q)) or p==q ):
                q = int(input("\n Enter q , should be prime and != p : "))


    else:
        p = 2475730193
        q = 908416969
        
    bob.p = p
    bob.q = q
    # set value of e and n for both sender and receiver 
    bob.e = ut.generate_e(bob.p,bob.q)
    bob.n = bob.p * bob.q

    alice.e = bob.e
    alice.n = bob.n

    #--------------------------------------- attack ----------------------

    # alice will send message to bob
    M = input("type the message to be sent : > ")
    cipher_text= alice.encrypt(M)   
    
    # save the cipher , n and e  in a text to simulate the attack by eva
    with open('ciphers.txt', 'w') as f:
        f.write(str(ut.str2int(cipher_text)) + "\n")
        f.write(str(bob.e) + "\n")
        f.write(str(bob.n) + "\n")
    f.close() 

    # Eva entercpt ciphers , e and n
    attacker = open("ciphers.txt", "r")
    lines = attacker.read().splitlines()
    attacker.close()
    C = int(lines[0])
    e = int(lines[1])
    n = int(lines[2])

    #-------------------------------------------------------------
    #                     Run the program 
    #-------------------------------------------------------------
    while True:
        attack_type = input("please enter the attack type : ")
        if attack_type == '.':
            break
        elif int(attack_type) == 1:
            deciphered_text = CCA(C,e,n)
            with open('CCA_outputs.txt', 'a') as f:
                    f.write("original message: " + M + "\n")
                    f.write("attacker output : " + deciphered_text + "\n")
            f.close()
        elif int(attack_type) == 2:
            deciphered_text = mathematical_attack(ut.int2str(C),e,n)
            with open('MA_outputs.txt', 'a') as f:
                
                    f.write("original message: " + M + "\n")
                    f.write("attacker output : " + deciphered_text + "\n")
            f.close()
        else:
            print("please chose one of the options ")






