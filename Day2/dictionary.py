data = {
    "name": "Ram",
    "age" : 20
}

print(data.keys())
print(type(data.keys()))
print(data.values())
print(type(data.values()))
print(data.items())
print(type(data.items()))

print(data)
data.update({"DOB": 2000})
print(data)

print("\nUsing Loops")
for x, y in data.items():
    print(x, y)

print("Last inserted item was:",data.popitem())# Removes the last inserted key-value pair
print(data.get("age"))# returns none if not found

data.clear()
print(data)

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)
