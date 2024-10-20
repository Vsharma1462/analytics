import random

letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number=[0,1,2,3,4,5,6,7,8,9]
special_char= ['@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '|', '\\', ':', ';', '<', '>', ',', '.', '?', '/']

num_letters=int(input("enter no. of letter"))
num_number=int(input("enter no. of number"))
num_special_char=int(input("enter no. of special char"))

password=[]

for i in range(1,num_letters+1):
    char=random.choice(letters)
    password += char

for i in range(1,num_special_char+1):
    char1=random.choice(special_char)
    password += char1

for i in range(1,num_number+1):
    char3=random.choice(number)
    password += str(char3)   


random.shuffle(password)
#print(password)

password_list=""
for char in password:
    password_list += char

print(password_list)




