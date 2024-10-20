# operator overloading is used to operate  on objects,like addition of two objects
class complex_num:
    def __init__(self,r,i):
        self.real =r
        self.imaginary=i

    def __add__(self,other):
       # return f"{self.real+other.real} + {self.imaginary+other.imaginary}i"
        return str(self.real+other.real) +"+"+ str(self.imaginary+other.imaginary)+"i"    
    
c1=complex_num(1,2)
c2=complex_num(4,5)
print(c1+c2) 


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __gt__(self,other):
        if self.age>other.age:
            return True
        else:
            return False    

p1=person("ram",32)
p2=person("shyam",23)
if p1>p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay")            
    
    



