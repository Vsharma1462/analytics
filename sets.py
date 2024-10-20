# sets do not allow duplicates
# sets are unordered so cant use indexing to acces elements so sets are not subcriptable
# sets does not support item assignment
#{} is dictionary    

set1={1,2,3,'a','b','c',True,1.5}
set1.add(99)
print(set1)
print(len(set1))
set1.remove(99)
print(set1)

set1.discard(1)                 # does not give error
print(set1)

print(set1.pop())
print(set1)

set1.add((1,3,5))                  # tuples can be added but list can not be added
print(set1)

# set methods

set2={1,2,3,4,5,6,7}
set3={5,6,7,8,9,10}
set4={21,22,32,33,34}
a=set2.union(set3)
b=set2.union((11,12))                  # tuples can be union with set
print(b)
print(a)
print(set2 | set3)

set3.update(set4)
print(set3)

print(set2.intersection(set3))