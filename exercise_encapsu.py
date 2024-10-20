#creating a bank account

class bank_account:
    def __init__(self,name,balance=0):
        self.name=name
        self.__balance=balance

    def __str__(self):
        return f"{self.name} : {self.__balance}"    

    def deposit(self,amount):
        self.__balance = self.__balance + amount
        print(f"deposited {amount} to your account")

    def withdraw(self,amount):
        if amount>self.__balance:
            print("not enogh balance")
        else:
            self.__balance=self.__balance-amount  
            print("successfully withdrew")  

    def get_balance(self):   #public method to get access private attribute
        return self.__balance        

obj=bank_account("vikash",1000)
obj.deposit(1000) 
#obj.withdraw(500) 
obj.withdraw(200)            
print(obj.get_balance())