def aes_128(text,key):
    text=bin(int(text,16)).replace("0b","0"*(128-len(text)-2))
    key=bin(int(text,16)).replace("0b","0"*(128-len(text)-2))
    ## matrice of message
    message_matrixe=[]
    message_key=[]
    for i in range(4):
        b=[]
        c=[]
        k=i
        for j in range(4):
            b.append(text[(i+k)*8:8])
            c.append(key[(i+k)*8:8])
            k+=4
        message_matrixe.append(b)
        message_key.append(c)

    for i in range(4):
        for j in range(4):
            message_matrixe[i][j]=exor(message_matrixe[i][j],message_key[i][j])
    sbox_aes=[['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '1', '67', '2b', 'fe', 'd7', 'ab', '76'],['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'], ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'], ['4', 'c7', '23', 'c3', '18', '96', '5', '9a', '7', '12', '80', 'e2', 'eb', '27', 'b2', '75'], ['9', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'], ['53', 'd1', '0', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'], ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '2', '7f', '50', '3c', '9f', 'a8'], ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'], ['cd', 'c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'], ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', 'b', 'db'], ['e0', '32', '3a', 'a', '49', '6', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'], ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '8'], ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'], ['70', '3e', 'b5', '66', '48', '3', 'f6', 'e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'], ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'], ['8c', 'a1', '89', 'd', 'bf', 'e6', '42', '68', '41', '99', '2d', 'f', 'b0', '54', 'bb', '16']]
    for i in range(len(message_matrixe)):
        for j in range(len(message_matrixe[0])):
            message_matrixe[i][j]=sbox_aes[int(message_matrixe[i][j][0:4],2)][int(message_matrixe[i][j][4::],2)]
    ##shift row left
    for i in range(4):
        a=[]
        k=i-1
        while len(a)<4:
            a.append(message_matrixe[i][(k+1)%4])
            k=(k+1)%4
        message_matrixe[i]=a[:]


    ##mix column
    mix_column=[[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
    new_matrix_message=[]
    for i in range(4):
        b=[]
        for j in range(4):
            somme="00000000"
            for k in range(4):
                message = ""
                if mix_column[i][k]==2 :
                    message=if2(message_matrixe[j][k])
                elif mix_column[i][k]==3:
                    message=exor(message_matrixe[j][k],if2(message_matrixe[j][k]))
                somme=exor(somme,message)
            b.append(somme)
        new_matrix_message.append(b)
        







def exor(a,b):
    exor=""
    for i in range(len(a)):
        if a[i]!=b[i]:
          exor+="1"
        else:
            exor+="0"
    return exor
def if2(message_matrixe):
    message = ""
    if message_matrixe[0] == "0":
        message = message_matrixe[1::] + "0"
    else:
        message2 = message_matrixe[1::] + "0"
        message = exor(message2,"00011011")
    return message

