number=[1,2,3,[4,5,6],7,8,9]
a=len(number)
print(a)
print(number[3][0])


num=[1,2,3,[4,[5,8,9],6],7,8,9]
num[3][1][1]='x'
print(num)

row1=['@','@','@']
row2=['@','@','@']
row3=['@','@','@']
matrix=[row1,row2,row3]
matrix[2][2]='x'
print(f"{row1}\n{row2}\n{row3}")

