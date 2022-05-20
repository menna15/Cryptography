import utils as ut
import math

class receiver:
    
    # set e as a public data member as it will sent to the sender as a public key
    e   = 0
    p = 0
    q = 0
    n = 0
    # set d as a private data members to the class
    __d = 0

    def set_parameters(self, e , n):
        self.e = e
        self.n = n

    # function to calculate the private key of the receiver
    def __calc_private_key(self):
        phi=(self.p - 1)*(self.q - 1)
        self.__d =ut.InvertModulo( self.e , phi)
        
    # function responsible for the decryption process
    def decrypt(self,C):
        receiver.__calc_private_key(self)
        dec_C=ut.str2int(C)
        dec_M=ut.PowMod(dec_C, math.floor(self.__d) , self.n)
        M=ut.int2str(dec_M)    
        return M