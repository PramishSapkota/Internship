import time

for i in range(3):
    print(f"Loading step {i}...", end="")
    time.sleep(1)
print("\nDone!")

'''
# python -u gives unbuffered o/p i.e we get to see the o/p as they come

while just using python we only get to see the final o/p.

# python -m runs the file as a module rather than script.
'''