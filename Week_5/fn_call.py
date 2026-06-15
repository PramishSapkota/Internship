def x(a=1,b=2):
    print("here")
    return(a+b)
    
print(x.__call__())
print(x())