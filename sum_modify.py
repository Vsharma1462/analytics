class summation:
    raise_sum=1
    def __init__(self,a, b):
        self.a=a
        self.b=b
    def sum(self):
        self.a *=summation.raise_sum
        self.b *=summation.raise_sum
        result = self.a + self.b
        print(result)
    

    @classmethod
    def modify(cls,newsum):
        cls.raise_sum *= newsum
        print(f"sum is multiplies by {cls.raise_sum}")
    
sum1=summation(2,3)
sum1.modify(10)
sum1.sum()


#method 2?>
class summation:
    a=2
    b=3
    c = a + b
    

    @classmethod
    def modify(cls,newsum):
        cls.c *= newsum
        print(f"new sum is {cls.c}")
        
c1 =summation
c1.modify(10)