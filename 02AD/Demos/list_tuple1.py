# tuples are immutable,ocuupies less memory space and more faster than list
# to create tuples we use () where as for creatin glist we use []

#List example
prime_numbers_list=[2,3,5,7,11]

#Tuple example
perfect_square_tuples=(1,4,9,16,25)

#Display Lengths
print("Lenght of List  Primes  :  ",len(prime_numbers_list))
print("Lenght of Tuple Square :  ",len(perfect_square_tuples))
print(80*"-")

#Iterate over both sequences
for p in prime_numbers_list:
    print("Prime Numbers : ",p)
print(80*"-")
for s in perfect_square_tuples:
    print("Square Numbers : ",s)

#diiference between list and tuples 1> syntax and 2> number of methods
print(20*"-"," List Methods ",20*"-")
list_methods=dir(prime_numbers_list)
i=1
for m in list_methods:
       print(i,':',m)
       i+=1
       #i++  #error
       

print(20*"-"," Tuples Methods ",20*"-")
#print(dir(perfect_square_tuples))
tuples_methods=dir(perfect_square_tuples)
i=1
for m in tuples_methods:
        print(i,':',m)
        i+=1
    #i++  #error
