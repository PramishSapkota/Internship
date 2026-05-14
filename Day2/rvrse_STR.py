word = input("Enter a string or number: ")
length = len(word) - 1
b = ""

for i in range(len(word)):
    b = b + word[length-i]

print(b)