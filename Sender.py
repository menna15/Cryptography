#!/usr/bin/env python

#-------------------------------------------------
#                      IMPORTS
#-------------------------------------------------
import asyncio
import time
import websockets
import random
import math
import json

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
#                 Encryption
#-------------------------------------------------

def cipher(m, e, n):
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
#       Start Transmission
#-------------------------------------------------
async def transmitt():
    async with websockets.connect('ws://localhost:8765') as websocket:
        firstTime = 0
        keys = await websocket.recv()
        keys = json.loads(keys)
        n = keys[0]
        e = keys[1]
        print(" Received < public key : ( e = {} , n = {})".format(e,n))

        msg = "{}".format("public key received")
        await websocket.send(msg)  

        while True:
            message = input("Message : ")
            message_dec = str2asci(message)
            print("encoding : {}".format(message_dec))
            time1 = time.time()
            encrypted = [cipher(i, e, n) for i in message_dec]
            time2 = time.time()
            # write the encryption time to a script
            if(not firstTime):
                f = open('result.txt','a')
                f.write("t = {}\n".format(time2-time1))
                f.close()
            ##
            s = json.dumps(encrypted)
            await websocket.send(s)
            print("sent > {}".format(s))
            firstTime = 1
            # try :
            #     received_msg = await websocket.recv()
            #     print("Received < {}".format(received_msg))
            # except websockets.exceptions.ConnectionClosed:
            #     break
            if message == 'close':
                    break

#-------------------------------------------------
#              Run the programe
#-------------------------------------------------

asyncio.get_event_loop().run_until_complete(transmitt())