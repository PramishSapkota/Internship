# Note: sth_update vannee fn name le set lai update garxa

a = {1,2,3}
b = {"a",'b','c',3}

print('Union')
print(a.union(b))
print(type(a.union(b)))
print(a)

print('\nIntersection')
print(a.intersection(b))
print(type(a.intersection(b)))

print('\nIntersection Update')
print(a.intersection_update(b))
print(type(a.intersection_update(b)))
print(a)

print('\nSymmetric Difference')
print(a.symmetric_difference(b))
print(type(a.symmetric_difference(b)))

print('\nSymmetric Difference Update')
print(a.symmetric_difference_update(b))
print(type(a.symmetric_difference_update(b)))
print(a)


print('\nUpdate')
a.update(b)
print(a)
print(type(a.update(b)))

print('\nAdd')
a.add("Addition")
print(a)

print("\nSuperset Subset")
s1={"a", "b", "c", 1, 2, 3}
s2={ 1, 2, 3}
print(s1.issuperset(s2))#true
print(s2.issuperset(s1))#False
print(s1.issubset(s2))#False
print(s2.issubset(s2))#true

print("\nRemove N Discard")
s1.remove(2) #if 2 wasnt present in s1 it would throw a key error
s1.discard(2)#here 2 isnt present still it doesnt throw an error
print(s1)

a = {1,2,3}
b = {"a",'b','c'}
a.update(b)
print(a)

# del is used to delete the entire set
# '''
# del(a)
# print(a) # gives NameError cuz a doesnt exist now
# '''

print("\nClear")#used to clear all item of the set
#i.e it makes an empty set
a.clear()
print(a)
