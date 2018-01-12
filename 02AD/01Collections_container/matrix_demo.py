# a is 2-D matrix with integers
a = [['Roy',80,75,85,90,95],
     ['John',75,80,75,85,100],
     ['Dave',80,80,80,90,95]]
print(a)
#b is a nested list but not a matrix
b= [['Roy',80,75,85,90,95],
    ['John',75,80,75],
    ['Dave',80,80,80,90,95]]
print(b)
#create dynamic matrix
n = 3
m = 4
x = [0] * n
for i in range(n):
    x[i] = [0] * m
print(x)

#Create a matrix using numpy in pyhton
from numpy import * 

x = range(16)

x = reshape(x,(4,4)) 

print(x)
# Accessing elements of the matrix in python by using list index
print(a[0])

print(a[0][1])

print(a[1][2])

#Accessing elements of the matrix in python by using negative list index
print(a[-1]) 
	
print(a[-1][-2]) 

print(a[-2][-3]) 

#Slicing a matrix in python using colon(:)  and numpy

stud = array([['Raj',80,75,85,90,95],
           ['Joy',75,80,75,85,100],
           ['Dale',80,80,80,90,95]])
print(stud[:3,[0,1]])

#Change elements of a matrix in python
n_stud=stud[0]
print(n_stud)

n_stud[1]=75
print(n_stud)

stud[2]=['Sam',82,79,88,97,99]
print(stud)

stud[0][4]=95
print(stud)
#Adding a new row in the matrix in python using append()

app_stud= append(stud,[['Smita',82,79,88,97,99]],0)
'''here 0 is axis that represents the dimensions where 0 stands for row
            and 1 stands for column'''

print(app_stud)

#Add a new column in the matrix for economics marks using insert().
in_stud= insert(app_stud,[6],[[73],[80],[85],[85]],axis=1) 
'''here axis represents the dimensions where 0 stands for row and 1 stands for column '''

print(in_stud) 

#Add a row in the matrix in python using +
y=[['Roy',80,75,85,90,95],
    ['John',75,80,75,85,100],
    ['Dave',80,80,80,90,95]]

y= y+ [['Sam',82,79,88,97,99]]

print(y)

#Delete a row of a matrix in python using delete from numpy
d= delete(a,[1],0)

print(d)

#Delete columns of a matrix in python using delete from numpy

dcol= delete(a, s_[1::2], 1)

print(dcol)



