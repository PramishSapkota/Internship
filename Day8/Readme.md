# Day 8 - Internship Journey

## Overview
Day 8 of my internship, focused on the collection module

## Topics Covered
- namedtuple 
- counter 
- defaultdict
- deque
- ChainMap 
- OrderedDict 
- UserDict 
- UserList
- UserString

## Key Learnings
- **namedtuple** is like a regular tuple but with named fields, making data more readable and accessible. It is like a class but with fixed attributes and no methods.

- **counter** is used to count the occurence. It returns a dictionary

- **defaultdict** is used to provide some default values for the key that does not exist and never raises a KeyError.

- **deque** is a double-ended queue, where the items can be added or removed from both left and right side. Unlike a queue where we can only do at right.

- **ChainMap** is used to combine dictionaries into one

- **OrderedDict** is used to make a dictionary ordered. It's functionalities like moving an entry to the end [move_to_end()], popping from left [popitem(last=False)] is still in use. Otherwise its mostly obsolute.

- **UserDict** is used to create a wrapper for dictionaries. We can add our own functions or change the functionalities or pre-existing functions

- **UserList** - Same as UserDict but for list.

- **UserString** - Same as UserDict but for list.


## Resources
- [collection_module](https://www.geeksforgeeks.org/python/python-collections-module/)


---

**Date:** May 20, 2026 