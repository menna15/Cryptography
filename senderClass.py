import utils as ut

class sender:

    n = 0
    e = 0 

    def encrypt(self,M):
        dec_M = ut.str2int(M) 
        while(dec_M > self.n):
            print("take care the other side cannot receive this message correctly as M > n which break RSA condition\n")
            print("please, reconsider and submit another message .. \n")
            M = input("type the message to be sent : > ")
            dec_M = ut.str2int(M)  
        dec_C = ut.PowMod(dec_M, self.e , self.n)
        C = ut.int2str(dec_C)
        return C
#----------------------------