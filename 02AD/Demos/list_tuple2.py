# tuples are immutable,ocuupies less memory space and more faster than list
# to create tuples we use () where as for creatin glist we use []

import timeit
#lets create 1000000 list and tuples and test it

list_test=timeit.timeit(stmt="[1,2,3,4,5]",number=1000000)
tuple_test=timeit.timeit(stmt="(1,2,3,4,5)",number=1000000)

print("List time: ",list_test)
print("Tuple time: ",tuple_test)
