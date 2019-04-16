"""Python Counter"""

from collections import Counter
from collections import namedtuple
from collections import defaultdict

#counter for list
counter_list = Counter(['a','b','c','a','c','a'])
print(counter_list)

issubclass(Counter, dict) #check is counter is a subclass of dict

#counter for string
counter_string = Counter('Addresss')
print(counter_string)

#counter for tuple
counter_tuple = Counter((1,2,1,3,4,1,2))
print(counter_tuple)

#counter for set - it only holds every value once.
counter_set = Counter({1,1,2})
print(counter_set)

#counter dict
counter_dict = Counter({'a':'test', 'b': 'test 2'})
print(counter_dict)


"""Python Named Tuple"""
pets = namedtuple('pets', ['name','age'])
fluffy = pets('flufy', 3)
print(fluffy)
print(fluffy.name)
print(fluffy._asdict())

"""Python DefaultDict """
def defaultvalue():
    return 0
otherdict=defaultdict(defaultvalue)
otherdict['a']=1
otherdict['b']=2
otherdict['c']=3
print(otherdict['b'])
print(otherdict['d'])
print(otherdict)