dictionary = { 
    "a1": 1,
    "a2": {"a3": 2},
    "a4": {"a5": 5, "a6": {"a7": 9}}
}

def flatten_dict(d, parent_key="", result=None):
    
    # Create result dictionary only once
    if result is None:
        result = {}
    
    for key, value in d.items():
        
        # Build full path
        new_key = f"{parent_key}.{key}" if parent_key else key
        # if some values exist in parent_key then lhs value is the new key else key is used
        
        # Recursive case
        if isinstance(value, dict):
            flatten_dict(value, new_key, result)
        
        # Base case
        else:
            result[new_key] = value
    
    return result


flattened = flatten_dict(dictionary)

print(flattened)