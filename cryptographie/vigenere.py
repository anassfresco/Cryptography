#built matrice vigenere

import string

def vigenre_crack(Plaintext,key):
    a = (string.ascii_lowercase)
    matrice = []
    for i in range(26):
        b = []
        for j in range(26):
            b.append(a[(i + j) % 26])
        matrice.append(b)
    new_key=""
    k=-1
    for i in Plaintext:
        if i!=" ":
            new_key+=key[(k+1)%len(key)]
            k=(k+1)%len(key)
        else:
            new_key+=" "
    cypher_text=""
    Plaintext=Plaintext.lower()
    new_key=new_key.lower()
    for i in range(len(Plaintext)):
        if Plaintext[i]==" ":
            cypher_text+=" "
        else:
            cypher_text+=a[(a.find((Plaintext[i]))+a.find((new_key[i])))%26]
    return Plaintext,new_key,cypher_text
def vigenre_dcrack(Plaintext,key):
    a = (string.ascii_lowercase)
    matrice = []
    for i in range(26):
        b = []
        for j in range(26):
            b.append(a[(i + j) % 26])
        matrice.append(b)
    new_key=""
    k=-1
    for i in Plaintext:
        if i!=" ":
            new_key+=key[(k+1)%len(key)]
            k=(k+1)%len(key)
        else:
            new_key+=" "
    cypher_text=""
    Plaintext=Plaintext.lower()
    new_key=new_key.lower()
    for i in range(len(Plaintext)):
        if Plaintext[i]==" ":
            cypher_text+=" "
        else:
            cypher_text+=a[(a.find((Plaintext[i]))-a.find((new_key[i])))%26]
    return cypher_text

print(vigenre_crack("THERE ARE TWO WAYS OF CONSTRUCTING A SOFTWARE DESIGN ONE WAY\
IS TO MAKE IT SO SIMPLE THAT THERE ARE OBVIOUSLY NO DEFICIENCIES AND THE OTHER WAY IS TO MAKE IT SO COMPLICATED THAT THERE ARE NO OBVIOUS DEFICIENCIES THE FIRST METHOD IS FAR MORE DIFFICULT","SYSTEM"))
