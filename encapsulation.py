"""Encapsulation is a fundamental principle of Object-Oriented Programming (OOP) that restricts direct access to certain components of an object,
 thereby protecting the object's integrity. This is typically achieved by bundling the data (attributes) and methods (functions) that operate on that 
 data into a single unit or class, and by using access modifiers to control visibility."""

"""Access modifier : Access modifiers in Python control the visibility and accessibility of class attributes and methods. They help encapsulate the data and maintain the integrity of 
objects by restricting how they can be accessed or modified from outside the class. Python has three main types of access modifiers:"""
#1.public attribute # 2. protected attribute(_) # 3. private attributet(__) # accesing private by public method and by namerangling

class student:
    def __init__(self,name,rollno,age):
        self.name=name
        self._rollno=rollno
        self.__age=age

    def __display(self):
        print(f"hi myself {self.name},{self.__age}years old with roll no {self._rollno} from student class") 

    def display_private(self):
        self.__display()               # accessing private attribute by using public ethod

class branch(student):
    def show(self):
        print(f"ny roll no is {self._rollno}")               


s1=student("rahul",23,20)
#print(s1.name)
#print(s1._rollno)
#print(s1.__age)

b1=branch("rahul",23,20)
#print(b1.name)
#print(b1._rollno)
#print(s1.__age)
#b1.show()
s1._student__display()             # accessing private attribute by name rangling but not recommended to a good programmer
print(s1._student__age)
