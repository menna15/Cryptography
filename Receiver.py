#!/usr/bin/env python

#-------------------------------------------------
#                      IMPORTS
#-------------------------------------------------
import asyncio
import websockets
import random
import math
import json

#-------------------------------------------------
#              Generation of primes
#-------------------------------------------------
def generate_prime(beg=7, end=10000):
    rand_number = random.randint(beg, end);
    if rand_number % 2 == 0:
        rand_number += 1
        
    for prime in range(rand_number, end, 2):

        isPrime = True
        for num in range(3, math.floor(prime/2), 2):
            if prime % num == 0:
                isPrime = False

        if isPrime:
            return prime


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

    for e in range(random.randrange(3, phi-1, 2), phi-1):
        if math.gcd(e, phi) == 1:
            return e


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
#-------------------------------------------------
#                 Decryption
#-------------------------------------------------

def decipher(m, e, n):
    return PowMod(m, e, n)

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
#                 Start Receiving
#-------------------------------------------------
async def Recieve(websocket, path):

    # keys 
    p = generate_prime()
    q = generate_prime()
    n = generate_n(p , q)
    e = generate_e(p , q)
    d = InvertModulo(e, (p-1)*(q-1))
    # write the key length to a script
    f = open('result.txt','a')
    f.write("n = {}\n".format(n))
    f.close()
    ##
    keys = [n,e]
    keys_list = json.dumps(keys)
    try :
        
        await websocket.send(keys_list)
        received_msg = await websocket.recv()
        print("Received < {}".format(received_msg))

        message = await websocket.recv()
    except websockets.exceptions.ConnectionClosed:
        asyncio.get_event_loop().stop()

    while True:
        print("Received < {}".format(message))
        s = json.loads(message)
        message_dec = [decipher(i, d, n) for i in s]
        decrypted = asci2str(message_dec)
        
        # msg = "{}".format("Correct")
        # await websocket.send(msg)  
        print("Message is : {}".format(decrypted))  

        if decrypted == 'close':
           asyncio.get_event_loop().stop()
        message = await websocket.recv()


            
start_server = websockets.serve(Recieve, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()