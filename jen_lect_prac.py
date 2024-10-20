
"""
# nested if ... else condition

height=int(input("what is ur hright :"))
if height >= 3:
    print("you can ride")
    age=int(input("enter ur age"))
    if age < 12:
        print("pay 150")
    elif age>12 and age<=18:
        print("pay 250") 
    else:
        print("pay 500")
else:
    print("cant ride")  
print("bye4")


# calculate bmi(body mass index)


weight=float(input("enter weight :"))
height=float(input("enter height :"))

bmi=weight/height ** 2
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

    
# calculate leap year

year=int(input("enter year :"))

if year % 4 == 0:
    
    if year % 100 == 0:
        
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")  

    else:
        print("leap year")          
else:
    print("leap yeAR")   

    
#  exercise - 2
    
height=int(input("what is ur hright :"))

if height >= 3:
    print("you can ride")
    age=int(input("enter ur age"))
    
    if age < 12:
        bill = 150
        print("pay 150")
    
    elif age > 12 and age <= 18:
        bill = 250
        print("pay 250") 
    
    else:
        bill = 500
        print("pay 500")

    want_photos =input("do u want photos:")
    if want_photos == 'y' or want_photos == 'Y':
        bill = bill + 50

    print(f"total : {bill}")       

else:
    print("can't ride")  
print("bye4")



# pizza order program  

size =input("enter size of pizza:")
bill = 0

if size =='s' or size =='S':
    bill +=100
    print("small size pizza")
elif size =='m' or size == 'M':
    bill +=200
    print("medium size pizza")
else:
    bill += 300
    print("large size pizza")

add_peproni =input(" do u want peproni :")
if add_peproni == 'y' or add_peproni =='Y':
    if size =='s' or size =='S':
        bill +=30

    else:
        bill += 50

extra_cheese=input("extra cheese :")
if extra_cheese =='y' or extra_cheese =='Y':
    bill += 30

print(f"total is {bill}")  


# creating love calculator

name1 = input("enter name :")
name2 =input("enter name2 :")
name =name1 + name2
lower_name =name.lower()

t=lower_name.count("t")
r=lower_name.count("r")
u=lower_name.count("u")
e=lower_name.count("e")

true=t+r+u+e

l=lower_name.count("l")
o=lower_name.count("o")
v=lower_name.count("v")
e=lower_name.count("e")

love=l+o+v+e

love_score= int(str(true) +str(love))

if love_score<10  or love_score>90:
    print(f" your score is {love_score}")
    
elif love_score>=40 and love_score<=50:
    print(f"your score is {love_score}")

else:
    print(f"your score {love_score}")   


 #random module
#randint,randrange,random,uniform(),choice(),shufle()

import random
a=random.randint(1,10)
a=random.randrange(1,10)
a=random.random()
a=random.uniform(1,3)
print(a)

list=[1,2,3,45,67,89,6] # creating  choice 
c=random.choice(list)
print(c)
random.shuffle(c)       # shuffle list
print(c)

# finding heads and tails

b=random.randint(0,1) 
if a == 0:
    print("tails")
else:
    print("heads")   


# who will pay the bill

import random
name=input("enter name separated by comma")
name_list=name.split(",")
print(name_list)

lenght=len(name_list)
bill_person=random.randint(0,lenght-1)
print(bill_person)

print(f"{name_list[bill_person]} will pay bill")

# method - 2
import random
name=['a','b','c']
lenght=len(name)
person=random.randint(0,lenght-1)
print(f"{name[person]} will pay bill ")

# program to calculate average height from a list of heights
heights=[10,20,30,40,50,50,60,70,80,90]

sum=0
for i in heights:
    sum+=i
average=sum/len(heights)
print(average)


sum=0
for i in range(1,10):
    sum+=i
average=sum/len(range(1,10))
print(average)

# finding the average of height without use of sum and len function

heights=input("enter heights :")

height_list=heights.split(" ")
count=0


for i in height_list:
    count +=1
print(count)  


for j in range(count):
    height_list[j]=int(height_list[j])
    
total =0
for k in height_list:
    total +=k
print(total)
avg = total/count  
print(round(avg))  

# finding max from a list without using a max function

number=input("enter number :")

num_list=number.split(" ")
count=0

for i in num_list:
    count +=1
print(count)  

for i in range(count):
    num_list[i]=int(num_list[i])

print(num_list)
 
max_num=num_list[0] 
for number in num_list:
    if number>max_num:
            max_num=number
print(max_num)

# sum of even number from 1 to 100
# method-1
sum=0
for i in range(2,101,2):
    sum+=i
print(sum)    

#method-2
sum=0
for i in range(2,101):
    if i % 2 == 0:
        sum+=i
print(sum)    

# fizzbuzz ,fizz ,buzz 
for i in range(1,16):
    if i % 3 ==0 and i % 5 == 0:
        print("fizbuzz")

    elif i % 3 == 0:
        print("fizz")

    elif i % 5 == 0:
        print("buzz")

    else:
        print(i)


# while loop 

number= 1

while number <=5:
    print(number)
    number +=1
print("out")


count=5

while count>0:
    print(count)
    count -= 1

    if count == 3:
        break

else:
    print("in else block")    
print("out")   

number=int(input("enter number :"))

while number != -1:
    
    print(number)

    number=int(input("enter number :"))
    
else:
    print("in else block")

print("out")

count=0
while True:
    print(count)
    count +=1

    if count == 5:
        break
else:
    print("in else block")
print("out")

total = 0 
number =int(input("enter number :"))
while number != 0 :
    total =total+number

    number =int(input("enter number :"))

else:
    print("in else block")

print("total is",total)   

# break, continue, pass

count=1
while count <=5:
    print(count)
    count +=1

    if count == 4:
        break
    print("hi")
else:
    print("in else block")
print("out")


count=1
while count<=5:
    print(count)
    count +=1

    if count == 4:
        continue
    print("hi")
else:
    print("in else block")
print("out")

count=1
while count<=5:
    print(count)
    count +=1

    if count == 4:
        pass
    print("hi")
else:
    print("in else block")
print("out")


string=["a",'b','c']
number=['hi','hello','wel']

for i in string:
    for j in number:
        print(i,j)

        if i == 'b' and j == 'hello':
            break

    print("out from inner")

print("out from outer")         

print("a")
try:
    a=int(input("enter a"))
    b=int(input("enter b"))
    print(a/b)



except (ZeroDivisionError,ValueError) as msg:
    print(msg)
    print(msg.__class__.__name__)
    

# exercise-21  
import math
def paint_cans(height,width,cover):
    area=height*width
    no_of_canes = math.ceil(area/cover)

    print(f"no of canes req for painting{no_of_canes}")

h=int(input("enter h"))
w=int(input("enter w"))
coverage=7
paint_cans(height=h,width=w,cover=coverage)

#exercise-22 finding prime number
import math
def find_prime(n):

    if n == 1:
        print("not prime")
        
    for i in range(2,math.ceil(n/2)+1):
        if n%i ==0 :
            print("not prime no.")

    else:

        print(" prime") 


n=int(input("enter n"))
find_prime(n) 

import math
def find_prime(n):

    if n == 1:
        return False

    if n%2 == 0:
        return False    
        
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0 :
            return False
 
    return True

n=int(input("enter n"))
print(find_prime(n))"""

# exercise-23

student_data={
    "a":92,
    "b":83,
    "c":73,
    "d":63,
    "e":53
}

grade={}

for student in student_data:
    marks=student_data[student]
    if marks>90:
        grade[student]="A+"

    elif marks>80:
        grade[student]="B+" 

    elif marks>70:
        grade[student]="C+"

    elif marks>60:
        grade[student]="D+"

    elif marks>50:
        grade[student]="E+"

    else:
        grade[student] ="f+"     

print(grade)                     




   









