'''
deque provides you with a double ended queue which means that you can append and delete elements from either side of the queue. 
'''
#First of all you have to import the deque module from the collections library:
from collections import deque

#Now we can instantiate a deque object.
d = deque()

#It works like python lists and provides you with somewhat similar methods as well. For example you can do:

d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))
# Output: 3

print(d[0])
# Output: '1'

print(d[-1])
# Output: '3'


#You can pop values from both sides of the deque:

d = deque(range(5))
print(len(d))
# Output: 5

d.popleft()
# Output: nothing

d.pop()
# Output: 4

print(d)
# Output: deque([1, 2, 3])

#We can also limit the amount of items a deque can hold.
#By doing this when we achieve the maximum limit of our deque it will simply pop out the items from the opposite end. It is better to explain it using an example so here you go:

d = deque(maxlen=30)


#Now whenever you insert values after 30, the leftmost value will be popped from the list. You can also expand the list in any direction with new values:

d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d)
# Output: deque([0, 1, 2, 3, 4, 5, 6, 7, 8])
