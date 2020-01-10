import math
import random
#import pyprimes
import warnings

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

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

p =5527064775949971276700546474393760569152256071781455112554572252477078482817219303694924773296938028736900310336193124455858291501008953781025760084204617
q =10263715010889663011237581846368625560721472564413404816414563312121711111200512062338133630430698017953660509772503749526855821347556114413740814256720609
n=p*q
c= 6016447327565519594114000681088119027251827426178525282923410539353402986195693266732998286093991346837854685945523958512316911535914428131590560765331415513592957120361162167163223354643895818554169459592360948153053758601978139504376688619229954806515113869761029037549195053798048200751500102605855423415
e = 67

k=gcd(c,n)
print(str(k))
phin=(p-1)*(q-1)
d=modinv(67,phin)

print(str(d))

m=pow(c,d,n);

print(str(m))