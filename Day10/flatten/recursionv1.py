dictionary = { 
    "a1": 1,
    "a2": {"a3": 2},
    "a4": {"a5": 5, "a6": {"a7": 9}}
}

def recr_fn(d):
    
    for key, value in d.items():
        
        print(key,end = "")
        if isinstance(value, dict):
            print(".",end="")
            recr_fn(value)
            # print(key,".")
        
        # Otherwise print final key-value pair
        else:
            print(f" = {value}")


recr_fn(dictionary)