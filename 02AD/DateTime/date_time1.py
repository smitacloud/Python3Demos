import datetime

#print(dir(datetime))
#print(help(datetime))
#how to create a date object

#Guido van Rossum
gvr_bday = datetime.date(1956,1,31)
print("Guido Van Rossum Birthday :",gvr_bday)

print("Year  : ",gvr_bday.year)
print("Month : ",gvr_bday.month)
print("Day   : ",gvr_bday.day)


#timedelta to add or substract date

y2k = datetime.date(2000,1,1)
dt = datetime.timedelta(100)
#negative number will decrease the date
print("100 days before crazy day : ",y2k-dt)
#positive number will increase the date
print("100 days after crazy day : ",y2k+dt)

now=datetime.datetime.today()
print("Today : ",now)
print("microsecond : ",now.microsecond)

#formatting Date
print("Converting date to string with strftime() function : ",gvr_bday.strftime("%A,%B %d,%Y"))
