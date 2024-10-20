class A:
    def display(self):
        print("from A")

class B(A):

    def display(self):
        print("from B")

class C:
    def show(self):
        print("from c")

class D(B,C):
    def display(self):
        print("from D")

d1=D()
d1.display()
print(D.mro())                