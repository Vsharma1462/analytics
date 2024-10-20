class Human:

    def __init__(self,num_heart):
        print("calling from human")
        self.num_eyes=2
        self.num_heart=num_heart

    def eat(self):
        print("i can eat")

    def work(self):
        print("i can work") 
    

class Male(Human):

    def __init__(self,name):
        print("calling from male")
        self.name=name
    

    def sleep(self):
        print("i can sleep")

    
class boy(Male):

    def __init__(self,num_heart,name ,dance):
        Human.__init__(self,num_heart)
        Male.__init__(self,name)
        self.dance=dance
        
    def work(self):
        #Human.work(self)
        super().work()
        print("i can code") 

class programmer(boy):
    def work(self):
        print("i can program")
    

boy1=boy(1,"vik",True)
print(boy1.dance)


