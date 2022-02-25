import random
import math
def prime_number(number):
    if number<=1:
        return False
    bool=True
    i=0
    while bool and i<10:
        a=random.randint(2,number)-1
        if (a**(number-1))%number!=1:
            bool=False
        i=i+1
    return bool
print(prime_number(431))
def integer(number):
    liste=[number]
    b=1
    i=0
    while i<b:
        a = []
        for k in range(2, math.ceil(math.sqrt(liste[i]))):


            if  prime_number(k) and liste[i]% k == 0:
                a.append(k)
        if len(a)!=0:
            h=a[0]
            for l in a:
                if not (prime_number(liste[i]/l)):
                    h=l
                    break
            liste+=[h,liste[i]/h]
            liste[i]=None
            b=b+2
        i=i+1

    for i in liste:
        if i==None:
            liste.remove(None)
    return liste
print(integer())