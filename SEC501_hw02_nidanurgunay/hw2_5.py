import copy


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

    while (i < n):
        delta = 0
        clen = len(C)
        for j in range(0, clen):
            delta ^= (C[j] * s[i - j])
        if delta == 1:
            dif = i - m
            PolCopy(T, C)
            nlen = len(B) + dif
            if (clen >= nlen):
                for j in range(dif, nlen):
                    C[j] = C[j] ^ B[j - dif]
            else:  # increase the degree of C
                for j in range(clen, nlen):
                    C.append(0)
                for j in range(dif, nlen):
                    C[j] = C[j] ^ B[j - dif]
            PolPrune(C)
            if L <= i / 2:
                L = i + 1 - L
                m = i
                PolCopy(B, T)
        i = i + 1
    return L, C


# Example usage
import random
x1 = [1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0]

x2 = [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x3 = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1]

length = 100




def num1and0 (x):
    count0=0
    count1=0
    for i in range (len(x)):
        if x[i]==0:
            count0+=1
        else:
            count1+=1
    return count0, count1



print(str(len(x1)))
print("for x1")
print ("L and C(x): ", BM(x1))
print("period of x1",FindPeriod(x1))
print("number of 0s and 1s in sequence", num1and0(x1))
print("for x2")
print ("L and C(x): ", BM(x2))
print("period of x2",FindPeriod(x2))
print("number of 0s and 1s in sequence", num1and0(x2))
print("for x3")
print ("L and C(x): ", BM(x3))
print("period of x3",FindPeriod(x3))
print("number of 0s and 1s in sequence", num1and0(x3))

