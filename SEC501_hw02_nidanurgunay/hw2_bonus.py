import binascii
import random


def PolPrune(P):
    n = len(P)
    i = n - 1
    while (P[i] == 0):
        del P[i]
        i = i - 1
    return i


def PolDeg(P):
    n = len(P)
    i = n - 1
    while (P[i] == 0):
        i = i - 1
    return i


# P gets Q
def PolCopy(Q, P):
    degP = len(P)
    degQ = len(Q)
    if degP >= degQ:
        for i in range(0, degQ):
            Q[i] = P[i]
        for i in range(degQ, degP):
            Q.append(P[i])
    else:  # degP < deqQ
        for i in range(0, degP):
            Q[i] = P[i]
        for i in range(degP, degQ):
            Q[i] = 0
        PolPrune(Q)

def BM(s):
    n = len(s)

    C = []
    B = []
    T = []
    L = 0
    m = -1
    i = 0
    C.append(1)
    B.append(1)

    while(i<n):
        delta = 0
        clen = len(C)
        for j in range(0, clen):
            delta ^= (C[j]*s[i-j])
        if delta == 1:
            dif = i-m
            PolCopy(T, C)
            nlen = len(B)+dif
            if(clen >= nlen):
                for j in range(dif,nlen):
                    C[j] = C[j] ^ B[j-dif]
            else: # increase the degree of C
                for j in range(clen, nlen):
                    C.append(0)
                for j in range(dif, nlen):
                    C[j] = C[j] ^ B[j-dif]
            PolPrune(C)
            if L <= i/2:
                L = i+1-L
                m = i
                PolCopy(B, T)
        i = i+1
    return L, C


def LFSR(C, S):
    L = len(S)
    fb = 0
    out = S[L - 1]
    for i in range(0, L):
        fb = fb ^ (S[i] & C[i + 1])
    for i in range(L - 1, 0, -1):
        S[i] = S[i - 1]

    S[0] = fb
    return out

def FindPeriod(s):
    n = len(s)
    for T in range(1, n + 1):
        chck = 0
        for i in range(0, n - T - 1):
            if (s[i] != s[i + T]):
                chck += 1
                break
        if chck == 0:
            break
    if T > n / 2:
        return n
    else:
        return T
# Takes a text and converts it to binary using ASCII encoding
def ASCII2bin(msg):
    M_i = []
    Mlen = len(msg)
    for i in range(0,Mlen):
        ascii_no = ord(msg[i])
        ascii_bin = bin(ascii_no)
        char_len = len(ascii_bin)
        if(char_len<9):
            for j in range(0,9-char_len):
                M_i.append(0)
        for j in range(2,char_len):
            M_i.append(int(ascii_bin[j]))
    return M_i

# Retransformation to see the decrypted message
def bin2ASCII(msg):
    res = list()
    for i in range(len(msg)//7):
        bins = msg[:7]
        str_bin = ''.join(str(x) for x in bins)
        res.append(chr(int(str_bin,2)))
        msg = msg[7:]
    return str(res)

def xor (s,d):
    l=len(s)
    arr=[0]*l
    for i in range (0,l):
        if (s[i]==d[i]):
            arr[i]=0
        else:
            arr[i]=1
    return arr


a=ASCII2bin("Dear Student")
print(a)
h=len(a)
print(str(h))
p=[]
ctext = [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0]
print("length of ctext", len(ctext))
for i in range (h):
    p.append(ctext[i])

print("Period of ctext",FindPeriod(ctext))
print(str(p))
key=[1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1]
print("Period of key",FindPeriod(key))
#print("BM for key", BM(key))
L, C= BM(key)
print(C)
keystream=[0]*868
initial=[1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,1]
print(initial)
for i in range (0,868):
    keystream[i]=LFSR(C,initial)
print (keystream)
print(str(len(keystream)))
m=xor(ctext,keystream)
print(m)
print(bin2ASCII(m))


