# tuples are immutable
# ordered
# tuples does not support item assignment

"""tuple1=(10,)                               # comma(,) is compulsory after 10 otherwise it counts as integer
tuple4=('a','b',1,2,1.2,1.3,True)
print(tuple4[0])                            # supports indexing
print(type4(tuple))
#tuple[0]=1                                assignment not supported
print(tuple4)
print(tuple4[1:4])                          # supports slicing
print(tuple4[1:4:2])                          # supports slicing
print(len(tuple4))                          # supports slicing

tuple2=(tuple4,tuple1)                     # nested tuple created
print(tuple2)
print(len(tuple2))
print(tuple2[0])

tuple3=tuple1+tuple                    # CONCATE TWO TUPLES
print(tuple3)
print(tuple3.count(10))
print(tuple3.index(2))

list = [1,2,3]                      # type version

print(tuple(list))"""


tuple1 =(10,)
tuple5=(10,)*5

print(tuple5)