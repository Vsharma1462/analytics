class student:
    def __init__(self,name,rollno,age):
        self.name=name
        self._rollno=rollno
        self.__age=age
    
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age>35:
            print("invalid")
        else:
            self.__age = age    


    """def __display(self):
        print(f"hi myself {self.name},{self.__age}years old with roll no {self._rollno} from student class") 

    def display_private(self):
        self.__display() 

class branch(student):
    def show(self):
        print(f"ny roll no is {self._rollno}") """


s1=student("rahul",23,20)
#s1._student__age = 45 # not recommendent to goog programmer
#s1._student__display() #not recommendent 
print(s1.get_age())
s1.set_age(34)
print(s1.get_age())

