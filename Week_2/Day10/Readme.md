# Day 10 - Internship Journey

## Overview
Day 10 of my internship, focused on dictionary flattening, multi-processing and multi-threading.

## Topics Covered
- Dictionary flattening 
- multi-processing 
- multi-threading

## Key Learnings
- Multi-processing uses different processors and are super fast while multi-threading uses multiple threads in a single processor but only one thread executes at a time depending on preemptive + GIL-controlled + opportunistic switching, often triggered by I/O or interpreter scheduling.

- Difference between multiprocessing, multithreading and async:

    -*Multiprocessing* is like 3 chefs in 3 different kitchen.

    -*Multithreading* is like 3 chefs in same kitchen sharing resources but only one is allowed to cook at a time. And they cook different meals.

    -*async* is one extremely efficient cook who switches the cooking between meals when one meal doesn't need much attention.

## Challenges Faced
- I initially tried to do the flattening using print statement as shown in recursionv1.py inside flatten folder. This approach worked well till "a4": {"a5": 5, "a6": {"a7": 9}}. Since i didn't saved the parent key it printed 'a6.a7:9' instead of 'a6.a7:9'. 

- This problem was solved using: 

```
new_key = f'{original_key}.{key}'if original_key else key
```

Now the parent key is saved using the dot as a separator. Now i can even save the flattened dictionary.

## Resources
- [StackOverflow](https://stackoverflow.com/questions/6027558/flatten-nested-dictionaries-compressing-keys)

- https://www.geeksforgeeks.org/python/python-value-list-key-flattening/

## Notes
<!-- Additional notes, code snippets, or observations -->

---

**Date:** May 22, 2026 