#Implementation of Diffe-Hellman Algorithm

import random

def isprime(num):
    for i in range(2,int(num/2)+1):
        if num%i==0:
            return 0
    return 1
    
def getRand():
    while True:
        n=random.getrandbits(20)
        if isprime(n):
            return n

#Random values...                        
p=getRand()
q=getRand()

#Alice and bob's private keys
a=random.getrandbits(10)
b=random.getrandbits(10)

R=q**a % p
S=q**b % p

#Secret keys for Alice and Bob respectively
Sa_key=S ** a % p
Sb_key=R ** b % p

print("Value of p= ",p)
print("Value of q= ",q)
print("Value of alice's private key (a)= ",a)
print("Value of Bob's private key (b)= ",b)
print("Secret key for Alice R_key= ",Sa_key)
print("Secret key for Bob S_key",Sb_key)