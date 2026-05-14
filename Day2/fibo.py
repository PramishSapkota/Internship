# fibonacci series using for
a = 0
b = 1

n = int(input("Enter how many Numbers of the series u want to see: ")) 

for i in range(1,n):
    print(b)

    c = a+b
    a=b
    b=c
