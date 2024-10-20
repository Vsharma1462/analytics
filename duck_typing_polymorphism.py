class Duck:
    def swim(self):
        print("i am a  duck and i can swim")

    def speaks(self):
        print("quack quack")

class Dog:
    def swim(self):
        print("i am a  dog and i can swim")

    def speaks(self):
        print("bark")

class person:
     def speaks(self):
        print("talks")

class Demo:                       # by using class method to display methodss

    def display(self,a):          # by using display function to call above methods having parameter a which reffered above classes Duck,Dog,person
        a.swim()
        a.speaks()
        print("info displayed")

d=Duck()
dog=Dog()
p=person()
demo=Demo()
demo.display(dog)                # passing dog,d,p object as argument in display function
demo.display(d)    
demo.display(p)        
