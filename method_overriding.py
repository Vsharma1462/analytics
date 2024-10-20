class father:
    def sleep(self):
        print("sleeps at 10pm")

    def eat(self):
        print("eating")    

class son(father):

     def sleep(self):
        print("sleeps at 12pm")           #method overriding and is runtime polymorphism type 
                                          # it occures in two classs
ram=son()
ram.sleep()





