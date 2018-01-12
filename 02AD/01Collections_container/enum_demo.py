'''
Another useful collection is the enum object.
It is available in the enum module, in Python 3.4 and up
(also available as a backport in PyPI named enum34.)
Enums (enumerated type) are basically a way to organize various things.

Let’s consider the User namedtuple. It had a type field.
The problem is, the type was a string.
This poses some problems for us.
What if the user types in Admin because they held the Shift key? Or ADMIN?
Or USER?

Enumerations can help us avoid this problem, by not using strings.
 Consider this example:
'''
from collections import namedtuple
from enum import Enum

class Users(Enum):
    admin=1
    user=2
    network_admin=3
    employee=4
    manager=5
    # The list goes on and on...
User = namedtuple('User', 'name age type')
perry = User(name="Perry", age=31, type=Users.admin)
chinky = User(name="Drogon", age=42, type=Users.network_admin)
tom = User(name="Tom", age=75, type=Users.manager)
smita = User(name="Smita", age=30, type=Users.manager)
charlie = User(name="Charlie", age=22, type=Users.employee)

# And now, some tests.
print("Is smita.type == tom.type : ",smita.type == tom.type)
print("charlie.type : ",charlie.type)

#There are three ways to access enumeration members
print("Users(1) : ",Users(1))
print("Users['admin'] : ",Users['admin'])
print("Users.admin : ",Users.admin)

