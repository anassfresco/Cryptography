import time
def generate_cle(key):#key hexa


    key=bin(int(key, 16))
    key=key.replace("0b","0"*(64-(len(key)-2)))
    permute_choice1=[57, 49, 41, 33, 25, 17, 9,
                     1, 58, 50, 42, 34, 26, 18,
                     10, 2, 59, 51, 43, 35, 27,
                     19, 11, 3, 60, 52, 44, 36,
                     63, 55, 47, 39, 31, 23, 15,
                     7, 62, 54, 46, 38, 30, 22,
                     14, 6, 61, 53, 45, 37, 29,
                     21, 13, 5, 28, 20, 12, 4 ]
    new_key=""
    for i in range(len(permute_choice1)):
        new_key+=key[permute_choice1[i]-1]
    leftkey=list(new_key)[0:len(new_key)//2]
    rightkey=list(new_key)[len(new_key)//2::]


    number_of_left_shift=[1, 1, 2, 2,
                            2, 2, 2, 2,
                            1, 2, 2, 2,
                            2, 2, 2, 1 ]
    liste_left=[]
    liste_right=[]
    for i in range(16):
        leftkey+=leftkey[0:number_of_left_shift[i]]
        del leftkey[0:number_of_left_shift[i]]
        liste_left.append(leftkey[::])
        rightkey+=(rightkey[0:number_of_left_shift[i]])
        del rightkey[0:number_of_left_shift[i]]
        liste_right.append(rightkey[::])

    permute_choice2=[14, 17, 11, 24, 1, 5,
                         3, 28, 15, 6, 21, 10,
                         23, 19, 12, 4, 26, 8,
                         16, 7, 27, 20, 13, 2,
                         41, 52, 31, 37, 47, 55,
                         30, 40, 51, 45, 33, 48,
                         44, 49, 39, 56, 34, 53,
                         46, 42, 50, 36, 29, 32 ]
    finalkey=[]
    for  i in range(16):
        range_key=liste_left[i]+liste_right[i]
        new_key=[]
        for j  in range(len(permute_choice2)):
            new_key.append(range_key[permute_choice2[j]-1])
        finalkey.append(new_key)
    return finalkey




def des_encryption(message,key):
    block_key=generate_cle(key)
    new_message = ""
    for i in message:
        new_message += format(ord(i), "x")
    new_message += "0D0A"
    blocks = []
    j = 0
    while j < len(new_message):
        m = j
        block = ""
        while j < len(new_message) and j < m + 16:
            block += new_message[j]
            j = j + 1
        blocks.append(block)
    if len(blocks[len(blocks) - 1]) < 16:
        blocks[len(blocks) - 1] = blocks[len(blocks) - 1] + ("0" * (16 - len(blocks[len(blocks) - 1])))
    ####apply IP
    initial_permutation_IP=[ 58, 50, 42, 34, 26, 18, 10, 2,
                             60, 52, 44, 36, 28, 20, 12, 4,
                             62, 54, 46, 38, 30, 22, 14, 6,
                             64, 56, 48, 40, 32, 24, 16, 8,
                             57, 49, 41, 33, 25, 17, 9, 1,
                             59, 51, 43, 35, 27, 19, 11, 3,
                             61, 53, 45, 37, 29, 21, 13, 5,
                             63, 55, 47, 39, 31, 23, 15, 7]
    print(blocks)
    binnary_blocks=[]
    for i in range(len(blocks)):

        binarry_block = bin(int(blocks[i], 16))
        binarry_block = binarry_block.replace("0b", "0" * (64 - (len(binarry_block) - 2)))
        new_blocks=""
        for j in range(len(initial_permutation_IP)):
            new_blocks+=binarry_block[initial_permutation_IP[j]-1]
        binnary_blocks.append(new_blocks)
    final_des=""
    final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
                      39, 7, 47, 15, 55, 23, 63, 31,
                      38, 6, 46, 14, 54, 22, 62, 30,
                      37, 5, 45, 13, 53, 21, 61, 29,
                      36, 4, 44, 12, 52, 20, 60, 28,
                      35, 3, 43, 11, 51, 19, 59, 27,
                      34, 2, 42, 10, 50, 18, 58, 26,
                      33, 1, 41, 9, 49, 17, 57, 25]

    print(binnary_blocks)
    for i in range(len(binnary_blocks)):
        left_block, right_block = binnary_blocks[i][0:32], binnary_blocks[i][32::]
        r0 = right_block
        print(len(r0))
        l0 = left_block
        for j in range(16):

            l1=r0
            r1=MAKE_R(r0,l0,block_key[j])
            r0=r1
            l0=l1
        concate=r0+l0
        new_concate=""
        for i in range(len(final_perm)):
            new_concate += concate[final_perm[i] - 1]

        final_des+= str(hex(int(new_concate, 2))).replace("0x","")+" "

    return final_des






def MAKE_R(R,L,K):
    Expansion_function = [32, 1, 2, 3, 4, 5, 4, 5,
                          6, 7, 8, 9, 8, 9, 10, 11,
                          12, 13, 12, 13, 14, 15, 16, 17,
                          16, 17, 18, 19, 20, 21, 20, 21,
                          22, 23, 24, 25, 24, 25, 26, 27,
                          28, 29, 28, 29, 30, 31, 32, 1]
    sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
             [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
             [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
             [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
            [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
             [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
             [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
             [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
            [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
             [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
              [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
              [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
             [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
              [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
              [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
              [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
            [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
             [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
             [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
             [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
            [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
             [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
             [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
             [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
            [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
             [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
             [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
             [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
            [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
             [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
             [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
             [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
    expantion_r=expantion(R,Expansion_function)

    final_exor=exor(expantion_r,K)

    block_box=[]
    i=0
    while i<len(final_exor):
        j=i
        text=""
        while j<i+6:
            text+=final_exor[j]
            j=j+1
        i=j
        block_box.append(text)


    sbox_r=""
    for i in range(len(block_box)):
        sbox_r1=(bin(sbox[i][int(block_box[i][0]+block_box[i][-1],2)][int(block_box[i][1:5],2)])).replace("0b","")
        if len(sbox_r1)<4:
            sbox_r1="0"*(4-len(sbox_r1))+sbox_r1
        sbox_r+=sbox_r1

    seconde_exor=exor(L,sbox_r)
    return seconde_exor


def expantion(mes,ip):
    new=""
    for k in range(len(ip)):
        new+=mes[ip[k]-1]
    return new

def exor(a,b):
    final_exor=""
    for j in range(len(a)):
        if a[j]!=b[j]:
            final_exor+="1"
        else:
            final_exor+="0"
    return final_exor




print(des_encryption("0123456789ABCDEF","133457799BBCDFF1"))
