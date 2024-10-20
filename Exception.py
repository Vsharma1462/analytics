class InvalidAmountError(Exception):
    pass
 
class InsufficientError(Exception):
    pass

class bank_account:
    def __init__(self,name,balance=0):
        self.name=name
        self.__balance=balance

    def __str__(self):
        return f"{self.name} : {self.__balance}"    

    def deposit(self,amount):
        try:
            if amount<=0:
                raise InvalidAmountError("amount must be greater than 1")
            self.__balance = self.__balance + amount
            print(f"deposited {amount} to your account")
        
        except InvalidAmountError as a:
            print(f"error is {a}")    
  
        finally:
            print("successfully deposited")

    def withdraw(self,amount):

        try:
            if amount>self.__balance:
                raise InsufficientError("amount is greater than my balnace")
            
            if amount<=0:
                raise InvalidAmountError("amount must be greater than 1")
            
            self.__balance=self.__balance-amount 
            print("successfully withdrew") 

        except (InsufficientError,InvalidAmountError) as s:
            print(f"error is {s}")

        finally:
            print("withdrew COMPLETED")       


    def get_balance(self):   #public method to get access private attribute
        return self.__balance    

object=bank_account("vikash",2000)
object.withdraw(500)        
print(object.get_balance())


