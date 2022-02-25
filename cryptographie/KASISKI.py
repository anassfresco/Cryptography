import time
a=["░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░──┐░░░░░░░",
"░░░░░░░░░│░░░░░░░░░░░░░░░░░░░░░┌─░░░│░░░░┌─░░░░└┬───░░░",
"░░│░░░┌─░│░░░░░░░░┌─░░░░│░░░░┌─┘░░░░│░░░┌┘░░░░░░│░░░░░░",
"░░│┌──┘░░├┐░░░░┌──┘░░░░░│░░──┘░░░░░░│░░┌┘░░░░░░░│░░░░░░",
"░░├┤░░░░░││░░┌─┘░░░░░░░░│░░│░░░░░░░░└┐┌┘░░░░░░░░│░░░░░░",
"░░│└┐░░░░││░░│░░░░░░░░░░│░┌┘░░░░░░░░░│└┐░░░░░░░░│░░░░░░",
"░░│░│░░░░│└┐░└──────┐░░░│░└─────┐░░░░│░└┐░░░░░░░│░░░░░░",
"░┌┘░└┐░░░├─│░░░░░░░░│░░░│░░░░░░░└┐░░░│░░└┐░░░░░░│░░░░░░",
"░│░░░│░░░│░│░░░░░░░┌┘░░░│░░░░░░░░│░░░│░░░└┐░░░░─┴──░░░░",
"░│░░░└┐░░│░└┐░░░░░░│░░░░│░░░░░░░░└┐░░└─░░░│░░░░░░░░░░░░",
"░│░░░░│░░│░░│░░░░░░│░░░─┘░░───────┘░░░░░░░░░░░░░░░░░░░░",
"░│░░░░└─░│░░│░─────┘░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"]
for i in a :
    print(i)
    time.sleep(0.4)

import string
from vigenere import vigenre_dcrack
from vigenere import vigenre_crack
plaintext="There are two ways of constructing a software design: \
One way is to make it so simple that there are obviously \
no deficiencies, and the other way is to make it so complicated \
that there are no obvious deficiencies. \
The first method is far more difficult."
hash=input("input your cypher text here ")

# hash="LFWKI MJCLP SISWK HJOGL KMVGU RAGKM KMXMA MJCVX WUYLG GIISW
# ALXAE YCXMF KMKBQ BDCLA EFLFW KIMJC GUZUG SKECZ GBWYM OACFV
# MQKYF WXTWM LAIDO YQBWF GKSDI ULQGV SYHJA VEFWB LAEFL FWKIM
# JCFHS NNGGN WPWDA VMQFA AXWFZ CXBVE LKWML AVGKY EDEMJ XHUXD"

cyphertext=hash.replace(" ","")

print(cyphertext)

def find_similar_words(hash):
    liste=[]
    distance=[]
    for i in range(len(hash)):

        for j in range(i+1,len(hash)):
            if hash[i]==hash[j]:
                m=i
                l=j
                text=""
                while m<len(hash) and l<len(hash) and hash[m]==hash[l] and hash[m]!=" " and hash[l]!=" ":
                    text += hash[m]
                    m=m+1
                    l=l+1
                if len(text)>=3 and all([text not in k for k in liste]):
                    liste.append(text)
                    distance.append(j-i)




    return liste,distance

print(find_similar_words(cyphertext))
def pgcd(a,b):
    a,b=max(a,b),min(a,b)
    while a!=b and a-b>=0:
        a,b=max(b,a-b),min(b,a-b)
    return a

same_words,distance=find_similar_words(cyphertext)
pgcd1=[]
for i in range(len(distance)):
    for j in range(i+1,len(distance)):
        if distance[i]!=distance[j]:
            pgcd1.append(pgcd(distance[i],distance[j]))
from collections import Counter
counter=Counter(pgcd1)

list_key=(sorted(counter, key=counter.get,reverse=True))
print(counter)
print(list_key)
key=0
for i  in list_key:
    if (counter[i]>key  and 3<i<20):
        key=i
    elif key!=0:
        break
print(key)

#####   get substring
list_substring=[]
for i  in range(key):
    k=i
    text=""
    while k<len(cyphertext):
        text+=cyphertext[k]
        k=k+key
    list_substring.append(text)
print(list_substring)
letters=[]
for i in list_substring:
    letter=[]
    alphabet=string.ascii_uppercase
    for j in alphabet:
        text=vigenre_dcrack(i,j)
        new_text=text.replace(" ","")
        counter=Counter(text)
        list_letter = list(sorted(counter, key=counter.get, reverse=True))
        if list_letter[0] in ["e","a","i","o","t"]:
            letter.append(j)
    letters.append(letter)
print(letters)

#####manuellemrnt
new_letter=[None]*6
for i in range(6):
    try:
        new_letter[i]=letters[i]
    except:
        new_letter[i]=[]
letters=new_letter
time.sleep(2)
for i in letters[0]:
    for j in letters[1]:
        for k in letters[2]:
            for l in letters[3]:
                for m in letters[4]:
                    for n in letters[5]:
                            print(i + j + k + l + m + n,vigenre_dcrack(hash, i + j + k + l + m + n))




















