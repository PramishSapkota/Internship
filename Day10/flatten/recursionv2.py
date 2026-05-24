dictionary = { 
    "a1": 1,
    "a2": {"a3": 2},
    "a4": {"a5": 5, "a6": {"a7": 9}}
}

def recr_fn(d, path=[]):
    
    for key, value in d.items():
        
        # Add current key to path
        path.append(key)
        
        if isinstance(value, dict):
            recr_fn(value, path)
        else:
            print(".".join(path), "=", value)
        
        # Remove current key after recursion finishes
        path.pop()


recr_fn(dictionary)