"""
import os
try:
    print("try")
    os._exit(0)
except ValueError:
    print("except")

finally:
    print("finally")


 # nested  try_except block execution sequence for different 14 cases
import os
import time
try:
    print("a")

    print("z")
    print("b")

    try:
        print("c")
        print("x")
        os._exit(0)
        print("d")

    except ZeroDivisionError:
        print("inner except")

    finally:
        print("inner finally block")

    print("out from inner block")             

except ZeroDivisionError :
    print("outer exception block")

finally:
    print("finally outer block")

print("out from outer try block")    


# nested try except block with time.sleep() for each step to delay by 2 seconds

import os
import time
try:
    print("a")
    time.sleep(2)
    print("z")
    time.sleep(2)
    print("b")
    time.sleep(2)

    try:
        print("c")
        time.sleep(2)
        print("x")
        time.sleep(2)
        print("d")

    except ZeroDivisionError:
        print("inner except")

    finally:
        print("inner finally block")

    print("out from inner block")             

except ZeroDivisionError :
    print("outer exception block")

finally:
    print("finally outer block")

print("out from outer try block")    


# using else block in try_except_finally block
# it will be executed only if there is no exception occured in try block
# else is used with exception block otherwise  it will give syntax error

try:
    print("try")
    #print(10/0)

except:
    print("exception")

else:
    print("else")

finally:
    print("finally")            

f=None
try:
    f=open('text.txt','r')

except:
    print("there is some problem while opening")

else:
    print("file opened successfully")
    print("#"*30)
    print(f.read())

finally:
    if  f is not None:
        f.close()
"""

import time
import threading
def print_a():
    time.sleep(2)
    print('a')
    
def print_b():
    time.sleep(0)
    print('b')
    
z=threading.Thread(target=print_a)
z.start() 
print(" current thrread :",threading.current_thread().getName())
t=threading.Thread(target=print_b)
t.start()
print(" current thrread :",threading.current_thread().getName())