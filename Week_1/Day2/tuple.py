# a= ("")
# print(type(a)) #<class 'str'>

# a= ()
# print(type(a)) #<class 'tuple'>

a = ("a","b","c","a",'x','y','z','a')

print(a.count('a'))
print(a.index('x'))

tup1 = ("a","b", "c")
temp = list(tup1)
temp.extend([1,2,3])
print(temp)
temp.pop(1)
print(temp)
tup1 = tuple(temp)
print(tup1)

