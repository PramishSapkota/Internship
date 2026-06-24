from collections import ChainMap

d1 = {"user": {"name": "John"}}
d2 = {"user": {"age": 20}}

cm = ChainMap(d1, d2)
a = d1 | d2
b = {**d1, **d2}
# c = d1 |= d2

print(a) # {'user': {'age': 20}}
print(b) # {'user': {'age': 20}}

print(cm.maps) # [{'user': {'name': 'John'}}, {'user': {'age': 20}}]
print(list(cm.keys())) # ['user']
print(list(cm.values())) # [{'name': 'John'}]

d1.update(d2) 
print(d1) # {'user': {'age': 20}}


# sabma pachiko value le replace garxa except chainmap
# ChainMap is view while other all are (shallow)copies

