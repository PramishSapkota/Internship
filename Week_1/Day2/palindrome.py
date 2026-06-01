word = input("Enter a string or number: ").lower()
b= str()
length = len(word) - 1
print(length)

for i in range(len(word)):
    b = b + word[length-i]
    print(b)

if word == b:
    print("Palindrome") 

else:
    print("Not Palindrome")

