# go from i= 1 to 7 when i=3 continue when i=5 break

i = 0

while i <= 6:
    if i == 3:
        i +=1
        continue
        
    print(i)
    i += 1


    if i ==5:
        break

    # i = i + 1

print("Out of loop")