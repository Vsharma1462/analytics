"""
-------------------------------------------------------------------------------------------------------------------------
# creating a thread without using a class
from threading  import *

def display():
    print("this code is executed by ",current_thread().getName())

# main thread creates child thread objects
# child thread object is responsible to execute display method(job)
       
t=Thread(target=display)
t.start()               # main thread starts childthread
print("this code is executed by ",current_thread().getName())   

from threading import *

def display():
    for i in range(10):
        print("cild")

t=Thread(target=display)
t.start()

for i in range(10):
    print("main")   
-------------------------------------------------------------------------------------------------------------------------
# getting and setting name of the thread

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

z.setName("vikash")
print(" current thrread :",threading.current_thread().getName())

t=threading.Thread(target=print_b)
t.start()
print(" current thrread :",threading.current_thread().getName())    

--------------------------------------------------------------------------------------------------------------------------    

# creating a thread by extending thread class

from threading import *

class mythread(Thread):
    def run(self):
        for i in range(10):
            print("child thread-1")

t = mythread()
t.start()

for i in range(10):
    print("main thread-1")  

-----------------------------------------------------------------------------------------------------------------------------    -

#  creating a thread without extending thread class           

from threading import *

class mythread:
    def display(self):
        for i in range(10):
            print("child thread-1")

obj = mythread()
t=Thread(target=obj.display)
t.start()

for i in range(10):
    print("main thread-1")        

---------------------------------------------------------------------------------------------------------------------------------
import time
from threading import *



def doubles(number):
    for i in number:
        print("double:",2*i)

def square(number):
    for k in number:
        print("square:",k*k)

number=[1,2,3,4,5]
begintime=time.time()

a=Thread(target=doubles,args=(number,))  
# print(a.getName())                        getting the name of thread
b=Thread(target=square,args=(number,)) 
# print(b.getName())
# a.setName("vikash")                       setting new name to thread
#print(a.getName())                         again getting the name of thread
a.start()
b.start()
a.join()
b.join()
endtime=time.time()
print("program ends in time:",endtime-begintime) 

-----------------------------------------------------------------------------------------------------------------------

# finding identification id of threads
from threading  import *

def test():
    print("child thread")

t= Thread(target=test)
t.start()
print("main thread id",current_thread().ident)
print("child thread id",t.ident)

--------------------------------------------------------------------------------------------------------------------------

# counting no of active threads is running
import time
from threading  import *

def test():
    print(current_thread().getName ,"started")
    time.sleep(3)
    print(current_thread().getName,"ended")

print("the no of active threads", active_count())
t1= Thread(target=test,name="child1")
t2= Thread(target=test,name="child2")
t3= Thread(target=test,name="child3")
t1.start()
t2.start()
t3.start()
print("no of active thread",active_count())
time.sleep(4)

print("no of active count",active_count())

-------------------------------------------------------------------------------------------------------------------------
# getting list of active thread running

import time
from threading  import *

def test():
    print(current_thread().getName ,"started")
    time.sleep(3)
    print(current_thread().getName,"ended")

#print("the no of active threads", active_count())
t1= Thread(target=test,name="child1")
t2= Thread(target=test,name="child2")
t3= Thread(target=test,name="child3")
t1.start()
t2.start()
t3.start()
#print("no of active thread",active_count())
#time.sleep(4)

#print("no of active count",active_count())

l=enumerate()
for t in l:
    print("name",t.name)
    print("id",t.ident)

time.sleep(10)

l=enumerate()
for t in l:
    print("name",t.name)

------------------------------------------------------------------------------------------------------------------------------

import time
from threading  import *

def test():
    print(current_thread().getName ,"started")
    time.sleep(3)
    print(current_thread().getName,"ended")

print("the no of active threads")
t1= Thread(target=test,name="child1")
t2= Thread(target=test,name="child2")
t3= Thread(target=test,name="child3")
t1.start()
t2.start()
t3.start()
print(t1.name ,"is alive",t1.is_alive())
print(t2.name ,"is alive",t2.is_alive())
print(t3.name ,"is alive",t3.is_alive())
time.sleep(4)


print(t1.name ,"is alive",t1.is_alive())
print(t2.name ,"is alive",t2.is_alive())
print(t3.name ,"is alive",t3.is_alive())

print("no of active count",active_count())

--------------------------------------------------------------------------------------------------------------------------


# join() method
# join() method is used when a thread wants to wait for another thread completion
# join method can be used with time like join(10) means 10 seconds

from threading import *
import time

def display():
    for i in range(10):
        print("child")
        time.sleep(2)
t=Thread(target=display)
t.start()
t.join()   
# in this main thread waits untill child thread completes 
# main thread works after child thread completed 
for i in range(10):
    print("main")

-------------------------------------------------------------------------------------------------------------
# Daemon thread
#The threads which are running in the background are called Daemon Threads.
#The main objective of Daemon Threads is to provide support for Non Daemon Threads( like main thread)

import time 
from threading import *

print(current_thread().isDaemon())
print(current_thread().daemon)
current_thread().setDaemon(True) # can not chnage status of main thread


#------------------------------------------------------------------------------------------------------------------
# changing the nature of child thread from non daemon to daemon

from threading import *

def job():
    print("child")

t=Thread(target=job)
print(t.isDaemon())
t.setDaemon(True) 
print(t.isDaemon()) 

-------------------------------------------------------------------------------------------------------"""

import time
from threading import *

def job():
    for i in range(10):

        print("child thread")
        time.sleep(2)

t=Thread(target=job)

t.setDaemon(True)
t.start()

time.sleep(5)
print("main thread")

 





