
import utils as ut
import receiverClass as rc
import senderClass as sc
import time
import matplotlib.pyplot as plt


bob = rc.receiver()
alice = sc.sender()


n_list = []
time_list = []
ciphers = open("ciphers.txt", "w")
p_q = open("test_cases.txt", "r")
lines = p_q.read().splitlines()
p_q.close()
i = 0
M = "Menna"
print(len(lines))
while (i < len(lines)):
    bob.p, bob.q = int(lines[i]), int(lines[i+1])
    i +=3
    # set value of e and n for both sender and receiver 
    bob.e = ut.generate_e(bob.p,bob.q)
    bob.n = bob.p * bob.q

    alice.e = bob.e
    alice.n = bob.n

    n_list.append(int(bin(bob.n).count("1")))
    start = time.time()
    cipher_text= alice.encrypt(M)  
    end = time.time()
    time_list.append(end - start)
    ciphers.write(str(ut.str2int(cipher_text)) + "\n")
    ciphers.write(str(bob.e) + "\n")
    ciphers.write(str(bob.n) + "\n")

ciphers.close() 


#ploting
plt.plot(n_list, time_list)

plt.xlabel('x - public key \'n\'')
plt.ylabel('y - time to encrypt')
plt.title('efficiency')

plt.show()