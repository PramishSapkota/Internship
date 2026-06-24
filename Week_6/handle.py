with open("Week_6/file.txt","r")as f:
    print(type(f))
    for line in f:
        print(line,end = '')
        # a = line.strip()
        # print(a)
        # print(type(a))

# print("new")
# with open("Week_6/file.txt","r")as file:
#     content = file.read()
#     linereader = file.readline()
#     print(type(content))
#     print(content.strip())