class Human:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"{self.name},{self.age}")    
        

    def eat(self):
        print("i can eat")

class Male(Human):

    def __init__(self, name, age,location):
        Human.__init__(self,name,age)
        self.location=location
    
    def sleep(self):
        print("i can sleep")

class Female(Human):

    def __init__(self, name, age,dance):
        Human.__init__(self,name,age)
        self.dance=dance
        

    def work(self):
        print("i can work")  

    def show(self):
        Human.show(self)
        print(f"know dancing:{self.dance}")      

female1=Female("vik",22,True)
female1.show()

