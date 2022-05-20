import math as math
import utils as cf
import receiverClass as rc
import senderClass as sc





p = 11
q = 13
modulo = p*q
exponent = cf.generate_e(120)

mySender = s.Sender()
mySender.p = p
mySender.q = q
mySender.e = exponent

ciphertext = mySender.encrypt("attack")
print(mathematical_attack(ciphertext, modulo, exponent))
