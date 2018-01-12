#Generator-Object : Generator functions return a generator object. Generator objects are used either by calling the next method on the generator object or using the generator object in a “for in” loop (as shown in the above program).
# A Python program to demonstrate use of 
# generator object with next() 
 
# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
  
# x is a generator object
x = simpleGeneratorFun()
 
# Iterating over the generator object using next
print(x.__next__()); # before Python 3, next()
print(x.__next__());
print(x.__next__());
