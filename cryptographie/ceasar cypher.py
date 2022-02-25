import string
from matplotlib import pyplot as plt
from collections import Counter

def crypt(text,private):
    a = list(string.ascii_lowercase)
    b = list(string.ascii_uppercase)
    dictioannary_lower = dict()
    dictionnary_upper = dict()
    k = 0
    for i in a:
        dictioannary_lower.update({i: k})
        k += 1
    j = 0
    for i in b:
        dictionnary_upper.update({i: j})
        j += 1
    new_text=""
    for i in text:
        if 97<=ord(i)<=122:
            car=a[(dictioannary_lower[i]+private)%26]
        elif 65<=ord(i)<=90:
            car=b[(dictionnary_upper[i]+private)%26]
        else:
            car=i
        new_text+=car
    return new_text
print(crypt("this is an example ",3))

def dcrypt(text,private):
    a = list(string.ascii_lowercase)
    b = list(string.ascii_uppercase)
    dictioannary_lower = dict()
    dictionnary_upper = dict()
    k = 0
    for i in a:
        dictioannary_lower.update({i: k})
        k += 1
    j = 0
    for i in b:
        dictionnary_upper.update({i: j})
        j += 1
    new_text=""
    index=0
    for i in text:
        if 97<=ord(i)<=122:
            car=a[(dictioannary_lower[i]-private)%26]
        elif 65<=ord(i)<=90:
            car=b[(dictionnary_upper[i]-private)%26]
        else:
            car=i
        new_text+=car
        index=i
    if crack(new_text):
        return "this is the crack"+new_text+"with private key"+index

print(crypt("this is an example ",3))
def cracking(text):
    for i in range(26):
        print(dcrypt(text,i))
def frequency_analysis(text):
    text=text.upper()
    x=Counter(text)
    return x

text="this is example"
analysis=frequency_analysis(text)
del analysis[" "]
x=[i for i in analysis.keys()]
y=[i for i in analysis.values()]
key=text.find(max(analysis))-text.find("E")
plt.bar(x,y)
plt.show()
print("possible key is " ,key)

#detect language
f = open("files.txt", "r")

for i in f:
    print(i)

def crack(i):
    if all([k in f.read() for k in i.split(" ")]):
        return True


