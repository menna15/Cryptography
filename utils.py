#-----------------------------------------------
#                 IMPORTS
#-----------------------------------------------
import random
import math
#-------------------------------------------------
#   Calculate m ^ e mod n
#-------------------------------------------------
def PowMod(m, e, n):
    if e == 0:
        return 1 % n
    elif e == 1:
        return m % n
    else:
        b = PowMod(m, e // 2, n)
        b = b * b % n
        if e % 2 == 0:
          return b
        else:
          return b * m % n
#-----------------------------------------------------
# Convert from string to int
#-----------------------------------------------------
def str2int (str):
    res = 0
    for i in range(len(str)):
        res = res * 256 + ord(str[i])
    return res
#-----------------------------------------------------
# Convert from int to string
#-----------------------------------------------------   
def int2str(dec):
    res = ""
    while dec > 0:
        res += chr(dec % 256)
        dec //=256
    return res[::-1]
#-------------------------------------------------
#       Convert String to List of ascii codes
#-------------------------------------------------
def str2asci(st):
    dec_list = []
    for i in st:
        dec_list.append(ord(i))
    return dec_list

#-------------------------------------------------
#       Convert List of ascii codes to String 
#-------------------------------------------------
def asci2str(dec):
    str_list = []
    for i in dec:
        str_list.append(chr(i))
    return ''.join(str_list)

#-------------------------------------------------
#             Extend Ecludiean
#-------------------------------------------------
def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)

#-------------------------------------------------
#  Generate d : the second number in private key
#-------------------------------------------------
def InvertModulo(e, phi):
    (b, x) = ExtendedEuclid(e, phi)
    if b < 0:
        b = (b % phi + phi) % phi # as we don't want -ve integers
    return b

#-------------------------------------------------
#   Generate n : the first number in public key
#-------------------------------------------------
def generate_n(p, q):
    return p * q

#-------------------------------------------------
#   Generate n : the second number in public key
#-------------------------------------------------
def generate_e(p, q):
    phi = (p-1) * (q-1)
    e = random.randint(2,phi) 

    while not math.gcd(e, phi) == 1:
       e = random.randint(2,phi)
    return e   

#-------------------------------------------------
#   Generate r 
#-------------------------------------------------           
def generate_r(n): 
    e = random.randint(2,n) 
    while not math.gcd(e, n) == 1:
       e = random.randint(2,n)
    return e 

#----------------------------------------------
# Check if prime
#----------------------------------------------
def prime(num):
   return num > 1 and all(num % i for i in range(2,int(math.sqrt(num))+1))
#-------------------------------------------------
#   Generate primes numbers with variable n bits 
#-------------------------------------------------      
def generate_primes(nbits):
    p = random.getrandbits(int(nbits/2))
    while(not prime(p)):
        p = random.getrandbits(int(nbits/2))
    q = random.getrandbits(int(nbits/2))
    while(not (prime(q)) or p == q):
        q = random.getrandbits(int(nbits/2))
    return p , q

# p,q=generate_primes(9)
# print(p,q)



