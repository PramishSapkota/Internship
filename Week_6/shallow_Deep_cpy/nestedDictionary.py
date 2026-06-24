import copy

a = {
    "x": 1,
    "y": {"inner": 10}
}
print("Original: ",a,"\n")
b = a.copy()
b["y"]["inner"] = 99

print("After Change")
print("Original: ",a)
print("Shallow: ",b)

print("\nFor deep copy")
a = {"x": 1,"y": {"inner": 10}}
print("Original: ",a)
b = copy.deepcopy(a)
b["y"]["inner"] = 99

print("After Change")
print("Original: ",a)
print("Deep: ",b)
