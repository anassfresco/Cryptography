import random
import string

def generate(plaintext):
    key=[]
    for i in range(len(plaintext)):
        if plaintext[i]!=" ":
            key.append(random.randint(0,len(plaintext)-1))
    return key
def vernam_crypt(plaintext,key):
    alphabet=string.ascii_uppercase
    plaintext=plaintext.upper()
    k=0
    cypher_text=""
    for i in range(len(plaintext)):
        if plaintext[i]==" ":
            cypher_text+=" "
        else:
            cypher_text+=alphabet[(alphabet.find(plaintext[i])+key[k])%26]
            k=k+1
    return cypher_text
def vernam_dcrypt(cyphertext,key):
    alphabet = string.ascii_uppercase
    k = 0
    plaintext = ""
    for i in range(len(cyphertext)):
        if cyphertext[i] == " ":
            plaintext += " "
        else:
            plaintext += alphabet[(alphabet.find(cyphertext[i]) - key[k]) % 26]
            k = k + 1
    return plaintext
key=generate("this is an example")
print(key)
print(vernam_crypt("this is an example",key))
print(vernam_dcrypt(vernam_crypt("this is an example",key),key))
