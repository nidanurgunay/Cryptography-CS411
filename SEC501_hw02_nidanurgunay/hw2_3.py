import math
import random
#import pyprimes
import warnings

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


#ax=b modn x=ba-1 modn
n1 = 333837116253674643166082492900
a1 = 57063337401967433471889139534
b1 = 397555361861029295385484594412


n2 = 333837116253674643166082492900
a2 = 176622984297114106732586191098
b2 = 84172329859897226978948124629

n3 = 333837116253674643166082492900
a3 = 320736651991764172584335713727
b3 = 30472957776104045808802882504




z1=modinv(a1,n1) #none
z2=modinv(a2,n2) #none
z3=modinv(a3,n3)

print("First a 's modular inverse is "+ str(z1))
print("Second a 's modular inverse is "+ str(z2))
print("Third a 's modular inverse is "+ str(z3))


x3=(b3*z3)% n3

print("third x is "+str(x3))


