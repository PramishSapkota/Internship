# Python program to find 
# squares of numbers in a given list
import time
import multiprocessing
import os

def square(n):
    # print("Worker process id for {0}: {1}".format(n, os.getpid()))
    return (n*n)

if __name__ == "__main__":
    # input list
    mylist = [_ for _ in range(1000)]

    # creating a pool object
    p = multiprocessing.Pool()
    start  =time.perf_counter()
    # map list to target function
    result = p.map(square, mylist)

    print(result)
    print("Time for Multiprocessing = ",time.perf_counter()-start)
    
    result = []
    
    start  =time.perf_counter()
    for num in mylist:
        result.append(square(num))

    print(result)
    print("\nTime for Single Process = ",time.perf_counter()-start,"\n")