import threading
import time

def sleeper_fn(n:int):
    print(f"Sleeping for {n} seconds")
    time.sleep(n)

#creating threads

t1 = threading.Thread(target= sleeper_fn, args=(1,))
#                                           ^
#                                           |
#                                           | 
# if using tuple need to put a comma at the end for single args
# but if there are 2 args dont need the comma at the end eg. below
# t1 = threading.Thread(target= sleeper_fn, args=(1,2))
t2 = threading.Thread(target= sleeper_fn, args=(2,))
t3 = threading.Thread(target= sleeper_fn, args=(4,))

# using list at args
# t1 = threading.Thread(target= sleeper_fn, args=[1])
# t2 = threading.Thread(target= sleeper_fn, args=[2])
# t3 = threading.Thread(target= sleeper_fn, args=[4])

# start threads
start = time.time() 
t1.start()
t2.start()
t3.start()

print(f"Finished execution in {start - time.time()}")

# waiting for completion