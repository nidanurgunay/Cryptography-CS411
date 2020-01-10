import math
from typing import Any

f = 1


#codes for generator
for i in range(0, 61):
    z=[0]*61

    x = i
    for j in range(0, 61):
        k = pow(x, j) % 61
        z[k] += 1#calculates the remainer of the jth power of x
    count = 0
    for k in range(1, 61):
        if z[k] != 0:
            count += 1
    if count == 60:#if all the numbers generated
        print(str(f)+"th "+'generetor number is ' + str(i))
        f=f+1


##THIS PART FOR THE SUBGROUP

w, h = 60, 60;
m = [[0 for x in range(w)] for y in range(h)]#creation of matrix
for i in range(0,60):
    for j in range (0,60):
        m[i][j]=((i+1)*(j+1)) % 61
        print(str(m[i][j]), end =' ')
    print("\n")

for i in range (0,60):
    z=m[0][i]# checked each column
    sub=str(z)
    k=z
    count=1
    while(k!=1):# code for finding subgroups
        k=m[k-1][i]#row
        sub=sub+" "+str(k)
       # z=k-1
        count+=1
    if count==5:
        print(str(i+1) + "s subgroup elements are " + sub )

#GENERATOR OF  5TH ORDER SUBGROUP
subel=[1,9,20,34,58]
for i in  range (0,5):
    k=subel[i]
    z=k
    print("for "+str(k),end=" ")
    for j in range (0,5):
        z=z*k
        t=z%61
        print (str(t),end=", ")
    print("\n")
