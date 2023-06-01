class complex:
    def __init__(self,r=0.0,i=0.0):
        self.re = r
        self.im = i

    def sum(self,c1):
        temp = complex()
        temp.re = self.re + c1.re
        temp.im = self.im + c1.im
        return temp

    def __add__(self, c):  # binary + is overloaded
        temp = complex()
        temp.re = self.re + c.re
        temp.im = self.im + c.im
        return temp

    def __invert__(self):
        temp = complex()
        temp.re = -(self.re)
        temp.im = -(self.im)
        return temp

    def show(self):
        print(self.re, "+", self.im, "i")


c1 = complex(2, 3.5)
print("The value of object1 : ")
c1.show()
c2 = complex(3.5, 2)
print("The value of object2 : ")
c2.show()
c3 = c1.sum(c2)
print("The sum of object1 and object2 through sum function: ")
c3.show()
c3 = c1 + c2
print("The sum of object1 and object2 through operator overloading: ")
c3.show()
c1 = ~c1
print("The negative of object 1 : ")
c1.show()