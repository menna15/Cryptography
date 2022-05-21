import utils as ut
import receiverClass as rc
import senderClass as sc
import time
import matplotlib.pyplot as plt


bob = rc.receiver()
alice = sc.sender()


n_list = []
time_list = []
p_q = open("test_cases.txt", "r")
lines = p_q.read().splitlines()
p_q.close()

ciphers_file = open("ciphers.txt", "r")
ciphers = ciphers_file.read().splitlines()
ciphers_file.close()

time_math = []
time_CCA = []
for cipher in ciphers:
    start = time.time_ns()
    deciphered_text = at.mathematical_attack(ut.int2str(cipher),e,n)
    time_math.append(time.time_ns() - start)

    start = time.time_ns()
    deciphered_text = at.CCA(cipher,e,n)
    time_CCA.append(time.time_ns() - start)


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


#ploting
plt.plot(n_list, time_list)

plt.xlabel('x - public key \'n\'')
plt.ylabel('y - time to encrypt')
plt.title('efficiency')

plt.show()