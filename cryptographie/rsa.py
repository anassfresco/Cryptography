import random
def pgcd(a,b):
    a,b=max(a,b),min(a,b)
    while a!=b and a-b>=0:
        a,b=max(b,a-b),min(b,a-b)
    return a

def egcd(a,b):
    if a==0:
        return b,0,1
    gcd,x1,y1=egcd(b%a,a)
    x=y1-(b//a)*x1
    y=x1
    return gcd,x,y

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


def rsa(a,b):
    n=a*b
    euler_function=(a-1)*(b-1)
    e=2
    while e<euler_function and  pgcd(e,euler_function)!=1 :
        e +=1

    d=egcd(e,euler_function)[1]
    return [(e,n),(d,n)]


def rsa_crypt(plain_text,rsa):
    liste=[]
    for i in plain_text:
        if i!=" ":
            liste.append(((ord(i))**rsa[0][0])%rsa[0][1])
        else:
            liste.append(" ")
    return liste

def rsa_decrypt(CHIFRE,rsa):
    plaintext=""
    for i in CHIFRE:
        if i!=" ":
            plaintext+=chr((i**rsa[1][0])%rsa[1][1])
        else:
            plaintext+=" "
    return plaintext

print(
    rsa_decrypt(
        rsa_crypt(
            "anas bahi is the best boy in the world ",
            rsa(73,23)
        ),
        rsa(73,23)
    )
)

