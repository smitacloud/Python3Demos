'''
A tuple is basically a immutable list
which allows you to store a sequence of values separated by commas.
They are just like lists but have a few key differences.
The major one is that unlike lists, you can not reassign an item in a tuple.
In order to access the value in a tuple you use integer indexes like:
'''
emp = ('Smita', 30)
print(emp[0])
# Output: Smita

'''
namedtuples? They turn tuples into convenient containers for simple tasks. With namedtuples you don’t have to use integer indexes for accessing members of a tuple. You can think of namedtuples like dictionaries but unlike dictionaries they are immutable.
'''
from collections import namedtuple

User = namedtuple('User', 'name password type')
perry = User(name="perry", password='perry123', type="admin")

print(perry)
# Output: User(name='perry', phone=9876543212, type="perry@gmail.com")

print(perry.name)
# Output: 'perry'

'''
`namedtuple` instances do not have per-instance dictionaries,
they are lightweight and require no more memory than regular tuples.
attributes in namedtuples are immutable
'''
User = namedtuple('User', 'name password type')
perry = User(name="perry", password='perry123', type="admin")
#perry.type=user #error
print(perry)

'''
You should use named tuples to make your code self-documenting. They are backwards compatible with normal tuples. It means that you can use integer indexes with namedtuples as well:
'''
Customer = namedtuple('Customer', 'name phone email')
perry = Customer(name="perry", phone=9876543212, email="perry@gmail.com")
print(perry[0])

#you can convert a namedtuple to a dictionary.
Customer = namedtuple('Customer', 'name phone email')
perry = Customer(name="perry", phone=9876543212, email="perry@gmail.com")
print(perry._asdict())
