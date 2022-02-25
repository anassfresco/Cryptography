import random
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return str(self.x)+"   " +str(self.y)


    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

class public_key:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class user():
    def __init__(self,key):
        self.key=key
        self.share_key=None
        self.private_key=None

class deffie_helman:
    def __init__(self,alice,bob,generate_point,public):
        self.alice=alice
        self.bob=bob
        self.generate_point=generate_point
        self.public=public
    def addition(self,point1,point2,function):
        m = (3 * (point1.x) ** 2 + function.a) / 2 * point1.y

        if point1!=point2:
            m = (point2.y - point1.y) / (point2.x - point1.x)

        x3 = m ** 2 - point1.x - point2.x
        y3 = m * (point1.x - x3) - point1.y
        return point(x3, y3)
    def calc(self,int,point3):
        binary=bin(int)[3::]
        point1=point3
        for i in binary:
            point1 = self.addition(point1, point1, self.public)

            if i == "1":
                point1 = self.addition(point1,point3, self.public)
        return point1
    def user(self):
        self.alice.share_key=self.calc(self.alice.key,self.generate_point)
        self.bob.share_key=self.calc(self.bob.key,self.generate_point)
    def private_key1(self,user1,user2):
        return self.calc(user1.key,user2.share_key)
    def private_key(self):
        self.alice.private_key=self.private_key1(self.alice,self.bob)
        self.bob.private_key=self.private_key1(self.bob,self.alice)

alice=user(100)
bob=user(2)
point1=point(1,1)
curve_poly=public_key(0,7)
echange=deffie_helman(alice,bob,point1,curve_poly)
echange.user()

echange.private_key()
print(echange.alice.private_key)
print(echange.bob.private_key)





















