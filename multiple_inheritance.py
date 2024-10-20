class Human:

    def __init__(self,num_heart):
        print("calling from human")
        self.num_eye=2
        self.num_nose=1
        self.num_heart=num_heart

    def eat(self):
        print("i can eat")

    def work(self):
        print("i can work")    

class Male:

    def __init__(self,name):
        print("calling from male")
        self.name=name

    def flirt(self):
        print("i can flirt")

    def work(self):
        print("i can code")        

class boy(Human,Male):

    def __init__(self,name,num_heart,language,):
        Human.__init__(self,num_heart)
        Male.__init__(self,name)
        self.language = language

    def sleep(self):
        print("i can sleep")

    def work(self):
        print("i can program") 

    def display(self):

        print(f"my name is {self.name}.i learn {self.language}.i have {self.num_eye} eyes,{self.num_nose} nose and {self.num_heart} heart")
boy1 = boy("vikash",1,"python")
boy1.display()