dictionary = {
    "a1":1,
    "a2":{"a3": 2},
    "a4": {"a5":5,"a6":{"a7":9}}
}

print(dictionary["a2"].keys())
print(dictionary["a4"].items())
print(dictionary["a4"].keys())
print(dictionary["a4"].values())

print(isinstance(dictionary,dict)) #true
print(isinstance(dictionary["a4"],dict),"\n") #true

# original_key = dictionary.keys()
def recr_fn(my_dict, original_key=''):
    for key, value in my_dict.items():

        new_key = f'{original_key}.{key}'if original_key else key
        
        if isinstance(value, dict):

            recr_fn(value, new_key)
        
            # If the value is also a dictionary, recursively process it
        else:
            print(f'{new_key}:{value}')
                # print(f'{value}')

recr_fn(dictionary)
