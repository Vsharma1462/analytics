class Human:

    def __init__(self,num_heart):
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart

    def eat(self):
        print("i can eat")

    def work(self):
        print("i can work") 

class Male(Human):

    def __init__(self,name,heart):
        super().__init__(heart)
        self.name=name

    def flirt(self):
        print("i can flirt")

    def work(self):
        super().work()                          # method over riding
        print("i can code") 

    def display(self):
        print(f"my name is {self.name} and i have {self.num_heart} heart and {self.num_eyes}eyes and {self.num_nose}nose")

male1=Male("vikash",1)
male1.display()   