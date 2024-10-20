class Demo1:                                   # method overloading is compile type polymorphism occures in single class
    def add(self,a,b,c=0):
        return a+b+c
    
d=Demo1()
print(d.add(2,3))
print(d.add(1,2,3))   

#method 2

class Demo2:
    def add(self,*args):
        total=0
        for i in args:
            total=total+i
        return total
    
d1=Demo2()
print(d1.add(2,3))
print(d1.add(1,2,3))   
print(d1.add(1,2,3,4,6,7,8,9))

        
