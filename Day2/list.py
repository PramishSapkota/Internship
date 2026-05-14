a= [11,2,31,4]

# '''
# # list function returns none so below code doesnt work as expected
# # print (a.append("xyz"))
# '''
# print(a.__doc__)

a.append("xyz")
print(a)

a.sort()# ascending order
print(a)

a.sort(reverse=True) #descending order
print(a)

a.reverse() # reverses the original list
print(a)

a= [11,2,31,2,4,2]
print(a.index(4))

print(a.count(2))

b = a 
#above line creates a reference of a on list variable b. Any changes on b will also change a. EG.
b[0]= "First"
print (a) # ['First', 2, 31, 2, 4, 2]
# so we need copy function
a= [11,2,31,2,4,2]
b = a.copy()
b[0]= "First"
print (a) # [11,2,31,2,4,2]

a.insert(1,3)
print(a)

b=["a","b",'c']
a.extend(b) # unpacks b and appends to b
print(a)

# appending dictionRY
c= [1,2,3]
d = {"a":1,
    "b": 2
}
c.append(d) # appends AS dictionary
print(c) #[1, 2, 3, {'a': 1, 'b': 2}]

c= [1,2,3]
d = {"a":1,
    "b": 2
}
c.extend(d.items()) # appends as tuple
print(c) # [1, 2, 3, ('a', 1), ('b', 2)]