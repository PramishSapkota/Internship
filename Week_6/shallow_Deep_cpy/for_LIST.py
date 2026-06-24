'''
copy() only copies the top-level structure without duplicating nested elements.
for nested elements same address reference is used 
so if  the nested element is mutable it can be changed
'''
import copy

original = [[1, 2], [3, 4],'immutable object']
print("Original: ", original,end="\n\n")

# Shallow copy: inner lists are shared
shallow = original.copy()
#       or
# shallow = copy.copy(original)
shallow[0].append(99)
print("After appending")
print("Original: ", original)  # [[1, 2, 99], [3, 4]] - Modified!
print("Shallow: ",shallow)
print("Changing string")
shallow[2] = 1
print("Original: ", original)
print("Shallow: ",shallow)

# Deep copy: inner lists are independent
print("\nDeep copy")
original = [[1, 2], [3, 4],'immutable object']
deep = copy.deepcopy(original)
deep[0].append(99)
print("Original: ", original) # [[1, 2], [3, 4]] - Unchanged 
print("Deep: ",deep)
print("\nChanging string")
shallow[2] = 1
print("Original: ", original) 
print("Deep: ",deep)
