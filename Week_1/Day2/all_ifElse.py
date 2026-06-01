# check vote eligibility

a = int(input("Enter your age: "))
if a >= 18:
    print("You can Vote")

elif a < 18 and a > 0:
    print("You cannot vote")

else :
    print("Invalid input")