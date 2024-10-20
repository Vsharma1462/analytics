#calculate bmi(body mass index)
class ZeroDivisionError(Exception):
    pass

class TypeError(Exception):
    pass

class BodyMassIndex:

    def __init__(self,weight,height):
        self.weight=weight                                          #weight=float(input("enter weight :"))
        self.height=height                                           #height=float(input("enter height :"))
     
    def cal_bmi(self):

        try:
            if self.height==0:
                raise ZeroDivisionError("can not devided by zero")
            if not isinstance(self.weight,(int,float)) and not isinstance(self.height,(int,float)):
                raise TypeError("height and weight must me integer")
            
            else:
                bmi=self.weight/self.height ** 2
                print(bmi)

                if bmi<18.5:
                    print("u r under wight")
                elif bmi>25 :
                    print("normal weight") 
                elif bmi>30 :
                    print("over weight") 
                elif bmi>35 :
                    print("too over weight")     
                else:
                    print("go to doctor") 


        except ZeroDivisionError as e:

            print(f"error is {e}")

        except TypeError as t:
            print(f"error is {t}")    

        finally:
            print("executed")  

bmi1=BodyMassIndex(60,1.57)            
bmi1.cal_bmi()  

bmi2=BodyMassIndex("a","b")
bmi2.cal_bmi()


    


 