"""try:
    num1=int(input("enter num1"))              #error handling by try.., except,else,finally
    num2=int(input("enter num2"))
    result= num1/num2
    print(result)
except ValueError:
    print("value error") 

except ZeroDivisionError:
    print("division error") 

else:
    print("divided suceesfully") 

finally:
    print("all i ok")

class library:                                   # example of class method
    total_book=0                                 #class attribute

    def __init__(self,title,author):             #creating instance method by __init__method 
        self.title=title                         #instance attribute1
        self.author=author                       #instance attribute2
        library.total_book +=1                  # increament total_book by 1

    def book_info(self):                                     #defining method for class library
        print(f"{self.title} of {self.author}")

    @classmethod                                             #defining class method
    def get_total_books(cls):
        print(f"total book in library:{cls.total_book}")    

    @classmethod                                             #defining class method
    def from_string(cls,book_string):
        title,author=book_string.split("by")
        return  cls(title,author)  

book1=library.from_string("abc by xyz")
book2=library.from_string("half girlfriend by chetan bhagat")

library.get_total_books()
book1.book_info()
book2.book_info()

class Counter:
    count = 0  # Class attribute to keep track of the number of instances

    def __init__(self):
        Counter.count += 1  # Increment the class-level count when a new instance is created

    @classmethod
    def get_count(cls):
        return cls.count  # Access class-level attribute using cls

# Create instances of Counter
c1 = Counter()
c2 = Counter()
c3 = Counter()

# Call the class method to get the count of instances
print(Counter.get_count())  # Output: 3

class human:
    def __init__(self,num_eyes,num_nose,num_heart):
        self.num_eyes=num_eyes
        self.num_nose=num_nose
        self.num_heart=num_heart
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")

class male(human):
    def __init__(self,name,eyes,nose,heart):
        super().__init__(eyes,nose,heart)
        self.name= name
    def work(self):
        super().work()
        print("i can code")
    def run(self):
        print("i can run") 
    def display(self):
        print(f"hi,i am {self.name} and i have {self.num_heart} heart,{self.num_eyes} eyes,{self.num_nose} nose")         

person=male("akash",2,1,1)
person.eat()
person.work()
person.run()
print(person.name)
print(person.num_eyes)
print(person.num_heart)
person.display()

class human:
    def __init__(self,num_heart):
        print("calling from human")
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart
    
    def eat(self):
        print("i can eat")
    
    def work(self):
        print("i can work") 

class male:
    def __init__(self,name):
        print("calling from human")
        self.name=name
    
    def flirt(self):
        print("i can flirt")  

    def work(self):
        print("i can code ")    

class boy(human,male):
 
    def __init__(self,name,heart,language):
        human.__init__(self,heart)
        male.__init__(self,name)
        self.language=language
    def work(self):
        print("i can test")
    
    def sleep(self):
        print("i can sleep")

    def display(self):
        print(f"Hi my name is {self.name} and i have {self.num_eyes} eyes,{self.num_nose} nose,{self.num_heart} heart.my language is {self.language}")   

boy1=boy("vikash",1,"hindi")
#boy1.eat()
#boy1.flirt()
#boy1.work()
#male.work(boy1)
#male.work(boy1)
#print(boy.mro())
boy1.display() 

def greet(func):                     # decorator example
    def wrapper():
        print("good morning")
        func()
        print("good night")
    return   wrapper

@greet
def hello():
    print("hello world")

hello()    

def logger(func):                        # decorator example
    def wrapper( *args, **kwargs):
        print("good morning")
        result = func(*args,**kwargs)
        print("good night")
        print(result)
        return result
    return   wrapper

@logger
def add(a,b):
     
     return a +b

add(2,5)    

# built-in decorator example

class employee:  
    #creating class attribute                 
    total_employee = 0
    raise_percentage = 1.05

# create attribute instance using constuctor method

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        employee.total_employee += 1

    def apply_raise(self):
        self.salary *= employee.raise_percentage
        print(f"new salary for {self.name} is {self.salary}")    

# create @classmethod decorator to set new percentage increase in salary of employee

    @classmethod    
    def set_raise_percentage(cls,percentage):
        cls.raise_percentage=percentage
        print(f"new set percentage is {cls.raise_percentage}")
    
    @classmethod

    def get_total_employee(cls):
        print(cls.total_employee) 

    @staticmethod
    def is_eligible_for_benefit(salary):
        if salary >50000:
            print("eligible")
        else:
            print("not eligible")    
    
emp1=employee("vikash",60000)
emp2=employee("vik",40000)    

#emp1.apply_raise()
#emp2.apply_raise()
#employee.set_raise_percentage(1.10)
#emp1.apply_raise()
#emp2.apply_raise()

#print(employee.is_eligible_for_benefit(emp1.salary))
#emp1.get_total_employee()
employee.is_eligible_for_benefit(emp1.salary)"""

