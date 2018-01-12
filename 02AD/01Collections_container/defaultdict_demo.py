from collections import defaultdict
'''
I personally use defaultdict quite a bit. Unlike dict, with defaultdict you do not need to check whether a key is present or not.
'''
paymodes=(
    ('1','cash'),
    ('2','credit card'),
    ('3','debit card'),
    ('4','net banking'),
    ('5','wallet'),
    )
pay_mode = defaultdict(list)

for pay_option ,mode in paymodes:
    pay_mode[pay_option].append(mode)

print(pay_mode)
'''
One other very important use case is when you are appending to nested lists inside a dictionary. If a key is not already present in the dictionary then you are greeted with a KeyError. defaultdict allows us to circumvent this issue in a clever way. First let me share an example using dict which raises KeyError and then I will share a solution using defaultdict.
'''
#some_dict = {}
#some_dict['option']['paymode'] = "cash"
# Raises KeyError: 'colours'


import collections
tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['option']['paymode'] = "cash"
# Works fine


#You can print some_dict using json.dumps. Here is some sample code:
import json
print("****************json*******************")
print(json.dumps(some_dict))
# Output: {"colours": {"favourite": "yellow"}}
