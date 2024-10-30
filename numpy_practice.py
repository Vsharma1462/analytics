"""import numpy as np

arr=np.array([1,2,3,4,5,6])

print(arr)
print(type(arr))
--------------------------------------------------------------------------------

import numpy as np

arr=np.array((1,2,3,4,5,6))

print(arr)
print(type(arr))
--------------------------------------------------------------------------------
# 0 - dimensional array
import numpy as np

arr=np.array(42)
print(arr)
------------------------------------------------------------------
# one dimensinal array
import numpy as np

arr=np.array([1,2,3,4,5])

print(arr)

------------------------------------------------------------------------
# two dimensinaol array
import numpy as np

arr=np.array([[1,2,3],[6,7,8]])

print(arr)
------------------------------------------------------------------------------
# three dimensional array
import numpy as np

arr=np.array([[[1,2,3],[6,7,8]],[[1,2,3],[6,7,8]]])

print(arr)

print(arr.ndim)

--------------------------------------------------------------------------
import numpy as np

arr=np.array([1,2,3,4] , ndmin=5)

print(arr)

print(arr.ndim)

------------------------------------------------------------------------
# indexing of one dimensinaol array
import numpy as np

arr=np.array([1,2,3,4,5])

print(arr[0])
-----------------------------------------------------------------------------------
# indexing of arrays
import numpy as np

arr=np.array([[1,2,3],[6,7,8]])

print(arr[1,2])
print(arr[0,-1])                          # negative indexing used to access the element

--------------------------------------------------------------------------------
# slicing of array 
import numpy as np

arr=np.array([1,2,3,4,5])


print(arr[0:4:2])               # 0 - start ,4 - end , 2 - step

arr=np.array([1,2,3,4,5,6,7,8,9,10])


print(arr[::2]) 
------------------------------------------------------------------------------

import numpy as np

arr=np.array([[1,2,3],[6,7,8]])

print(arr[1,1:3]) 

print(arr[0:2,2])

print(arr[0:2 , 1:3])   # this will return 2-d array
#------------------------------------------------------------------------------
import numpy as np

arr=np.array([[1,2,3],[6,7,8]])
arr1=np.array([1.2,1.3])

print(arr.dtype)
print(arr1.dtype)

----------------------------------------------------------------------------
import numpy as np
arr1=np.array(['a','b','c'])
print(arr1.dtype)
--------------------------------------------------------------

import numpy as np
arr1=np.array([1,2,3,4] , dtype='i4')

print(arr1)
print(arr1.dtype)

-----------------------------------------------------------------------------
# conerting one data typr to another data (type change)

import numpy as np
arr1=np.array([1,2,3,4])

newarr=arr1.astype("f")          # creating new variable using astype()

print(newarr)
print(newarr.dtype)

---------------------------------------------------------------------------

import numpy as np
arr1=np.array([1,2,3,4])

newarr=arr1.astype("bool") 

print(newarr)
print(newarr.dtype)
 
------------------------------------------------------------------------------ 
#The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

#The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

#The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

# copy

import numpy as np

arr1=np.array([1,2,3,4])

newarr=arr1.copy()

arr1[0]=v

print(newarr)
print(arr1)

----------------------------------------------------------------------------

import numpy as np

arr1=np.array([1,2,3,4])

newarr=arr1.view()

arr1[0]=42

newarr[0]=32

print(newarr)
print(arr1)

-------------------------------------------------------------------------------
#Every NumPy array has the attribute base that returns None if the array owns the data.Otherwise, the base  attribute refers to the original object

import numpy as np

arr1=np.array([1,2,3,4])

x=arr1.view()
y=arr1.copy()

print(x.base)
print(y.base)

--------------------------------------------------------------------------------------

import numpy as np

arr1=np.array([[1,2,3,4],[1,2,3,6]])

print(arr1.shape)

#The example above returns (2, 4), which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4

-------------------------------------------------------------------------------------
# advance indexing 
# by using nd array with required indexes then passing it as argument
# one dimensional array
import numpy as np
a=np.array([10,20,30,40,50,60,70,70,80,90])

indexes=np.array([0,2,7])
print(a[indexes ])

# method-2 by using list indexing

l=[0,2,7] 
print(a[l])
-------------------------------------------------------------------------------
# two dimensional array
import numpy as np

l = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

a=np.array(l)

print(a[[1,3],[0,2]])

print(a[[1,3],[1]])

print(a[[1,3],[1,2,3]])              # shape mismatch 


# a[[row index],[column index]]
--------------------------------------------------------------------------------

# advancing in three dimensional array

import numpy as np

l=[[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]

a=np.array(l)

# a[[index of 2d array],[row indexes],[column indexes]]

print(a[[0,1,1],[0,0,2],[0,1,3]])

print(a[[0,1],[1,0],[1,3]])
------------------------------------------------------------------------------

# advance indexing based on some condition using boolean array
import numpy as np

l=[10,-5,20,30,-3,-1,67]

a=np.array(l)

boolean_array=a<0

print(a[boolean_array])

print(a[a<0])

print(a[a>10])

print(a[a>15 ])

-------------------------------------------------------------------------------
import numpy as np

l=[[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]

a= np.array(l)

boolean_arry=a>20

print(a[boolean_arry])

print(a[a>20 ])

------------------------------------------------------------------------------------

# arithmatic operation in nd array
# one dimensional array

import numpy as np

l=[10,20,30,40]

a=np.array(l)

print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a%2)
print(a//2)
print(a**2)

-----------------------------------------------------------------------------------

# two dimensional array
import numpy as np

l=[[10,20,30,40],[50,60,70,80]]

a =np.array(l)

print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a%2)
print(a//2)
print(a**2)

--------------------------------------------------------------------------------

import numpy as np

l=[[[10,20,30,40],[50,60,70,80],[90,100,110,120]],[[130,140,150,160],[170,180,190,200],[210,220,230,240]]]

a=np.array(l)

print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a%2)
print(a//2)
print(a**2)


----------------------------------------------------------------------------------

import numpy as np 

l=np.array([1,2,3,4,5])

a=np.array([6,7,8,9])

print(np.add(l,a))

# ValueError: operands could not be broadcast together with shapes (5,) (4,)

-----------------------------------------------------------------------------------
import numpy as np 

l=np.array([1,2,3,4,5])

a=np.array([6,7,8,9,10])

print(np.add(l,a))

# result is [ 7  9 11 13 15] 

---------------------------------------------------------------------------------

import numpy as np 

l=np.array([[1,2,3,4,5],[6,7,8,9,10]])

a=np.array(l)

for x in np.nditer(a):
    print(x)

------------------------------------------------------------------------------
# change the data type of the array

import numpy as np 

l=np.array([[1,2,3,4,5],[6,7,8,9,10]])

a=np.array(l)

for x in np.nditer(a,flags=['buffered'],op_dtypes='float'):
    print(x)

# buffer is temporary memory space used to store op_dtypes of array 
----------------------------------------------------------------------------------
# indexing in sliced array

import numpy as np 

l=[[1,2,3,4,5],[6,7,8,9,10]]

a=np.array(l)

for x in np.nditer(a[:,:2]):
    print(x)

----------------------------------------------------------------------------------  
# ndenumerate used to give index as well as values
import numpy as np 

l=np.array([1,2,3,4,5,6,7,8,9,10])

a=np.array(l)

for index , x in np.ndenumerate(a):
    print(f"{x} in index {index}")


---------------------------------------------------------------------------------    
# two dimensinal array

import numpy as np 

l=[[1,2,3,4,5],[6,7,8,9,10]]

a=np.array(l)

for index , x in np.ndenumerate(a):
    print(f"{x} in index {index}")
--------------------------------------------------------------------------------------
import numpy as np 

a=np.array([1,2,3,4,5])

print(a+a)
print(a-a)
print(a*a)
print(a/a)
print(a%a)
print(a//a)
print(a**a)

-------------------------------------------------------------------------------
import numpy as np 

l=[[1,2,3,4,5],[6,7,8,9,10]]

a=np.array(l)

print(a+a)
print(a-a)
print(a*a)
print(a/a)
print(a%a)
print(a//a)
print(a**a)

------------------------------------------------------------------------------

# broad casting in numpy
# araays with diff dimension ,different shape ,different sizes ,
# arithmatic operation  can be performed with bradcasting
import numpy as np

a = np.array([10,20,30])
b =np.array([40])             # with broadcasting [40,40,40]

print(a+b)

----------------------------------------------------------------------------------
import numpy as np

a = np.array([10,20,30])
b =np.array([40])             # with broadcasting [40,40,40]

print(a+b)

------------------------------------------------------------------------
import numpy as np

l=[[1,2,3,4],[6,7,8,9]]

a = np.array(l)

b=np.array([1,2,3,4])
print(a.shape)

print(b.shape)

print(a+b)

---------------------------------------------------------------------------
import numpy as np

l=[[1,2,3,4],[6,7,8,9]]

a = np.array(l)

b=np.array([1,2,3 ])
print(a.shape)

print(b.shape)

print(a+b)

ValueError: operands could not be broadcast together with shapes (2,4) (3,)

-----------------------------------------------------------------------------------

import numpy as np

a=np.array([[10,20],[30,40],[50,60]])

b=np.array([10,20])

print(a.shape)

print(b.shape)

print(a+b)

---------------------------------------------------------------------------------
import numpy as np

a=np.array([[10,20],[30,20],[50,20],[60,20]])

b=np.array([10,20,30])

print(a.shape)

print(b.shape)

print(a+b) 

#ValueError: operands could not be broadcast together with shapes (4,2) (3,)

--------------------------------------------------------------------------------
#      reshape of arrays 

import numpy as np

a=np.array([1,2,3,4,5,6,7,8,9,10])

b=np.reshape(a,(5,2),order='C')

c=np.reshape(a,(5,2),order='F') 

d=np.reshape(a,(5,2),order='A') 



print(b)

print(c)

print(d)

----------------------------------------------------------------------------

import numpy as np

a=np.array([1,2,3,4,5,6,7,8,9,10])

b=np.reshape(a,(5,2),order='C')

c=np.reshape(a,(5,2),order='F') 

d=np.reshape(a,(5,2),order='A') 

b[0][0]=7777

print(b)

print(c)

print(d)
-----------------------------------------------------------------------------
#            second method for reshape i.e. ndarray object  method
import numpy as np   

a=np.array([1,2,3,4,5,6,7,8,9,10])

b=a.reshape((5,2),order='F')

print(b)

-----------------------------------------------------------------------------

import numpy as np

a=np.arange(1,25)

b=a.reshape((2,3,4),order='F')

print(b)

---------------------------------------------------------------------------------

import numpy as np

a=np.arange(1,11)
print(a)

b=a.reshape((-1,5))

c=a.reshape((5,-1))

print(b)

print(c)

 ---------------------------------------------------------------------

 # resize of arrays into any dimension

import numpy as np

a=np.arange(1,6)
 
b = np.resize(a,(2,4))

c=np.resize(a,(2,2))

#  d=a.resize((2,4))

print(b)

print(c)

----------------------------------------------------------------------------------

import numpy as np

a=np.arange(1,6)
 
b = a.resize((4,2))

# changes in existing array a,  not in b

# extra element neede for new shape will be filled with zeroes 

print(a)

print(b)

-------------------------------------------------------------------------------------
# flaten() converts n dimensinaol array  into an one dimensinal array

import numpy as np

a=np.arange(1,11).reshape(5,2)

b = a.flatten()

print(b)

---------------------------------------------------------------------------------
# flar return one dimensinal iterator array
import numpy as np

a=np.arange(1,7).reshape(3,2)

b = a.flat

for i in b:
    print(i)

print(b[5])

-----------------------------------------------------------------------------
# ravel() converts n dimensinaol array  into an one dimensional array view not an separate copy
# it is numpy library function  

import numpy as np

a=np.arange(1,7).reshape(3,2)

b = np.ravel(a)

c=a.ravel()        # ndarray method

print(c)

b[4]=10        # original array will be affected

print(a)

#------------------------------------------------------------------------------------------------ 
# concept of transpose()
# transpose two dimensinaol array
import numpy as np

a=np.arange(1,13).reshape(3,4)

#print(a)

b=np.transpose(a)

print(b)

----------------------------------------------------------------------------------------
#   transposing 3 dimensional array
import numpy as np

a=np.arange(1,25).reshape(2,3,4)

#print(a)

b=np.transpose(a)      # by default (4,3,2) dimension

print(b)

------------------------------------------------------------------------

import numpy as np

a=np.arange(1,25).reshape(2,3,4)

#print(a)

b=np.transpose(a,axes=(2,0,1))      # 2- column of a, 0- dimension of a, 1- dimension of rows of a

print(b)

----------------------------------------

import numpy as np

a=np.arange(1,25).reshape(2,3,4)

#print(a)

b=np.transpose(a,axes=(2,1,0))      # 2- column of a, 0- dimension of a, 1- dimension of rows of a

# shape of b is (4,3,2 )
print(b) 
---------------------------------------------------------------------


import numpy as np

a=np.arange(1,25).reshape(2,3,4)

#print(a)

b=a.transpose((2,0,1))

print(b)

----------------------------------------------------


import numpy as np
  
a=np.arange(1,25).reshape(2,3,4)

#print(a)

b=a.T

print(b)

-----------------------------------------------------------------"""

import mysql.connector

connection=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='12345',
    database='local'

)

my_cursor = connection.cursor()

connection.commit()

connection.close()

