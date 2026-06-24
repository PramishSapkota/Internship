# Week 5

## Overview
Week 5 of my internship experience, focusing on basic and  foundational concepts of python.


## Notes
- Inheritance in named tuple:

    Inheriting named tuple doesn't work like that of class. We need to modify the \_\_new__() function to take extra argument. And still that extra argument isn't taken in tuple

- Various dunder methods of a class exposed by dir.

    Learned about \_\_new__ , \_\_hash__ , \_\_getattribute__ and various others. These methods are inherited from the class object. Every class in python is a child class of class object. Due to this most people don't know abt these until dived deeper.

- Uses of async programming
    - **Multi-processing**: For CPU bound task. Heavy processing such as image, video precessing, training models etc.

    - **Multi-threading**: For I/O bound task. Waiting for input, fetching requests from server or APIs.

    - **async**: Same as multithreading but if the I/O tasks are in large quantity. Eg. for 10-20 or even 100 use threading but for greater than that use async. For larger tasks async is faster bcz the cost of multithreading will outweigh its benefit while async is lightweight routine. Basically for lots of waiting task

- GIL
    It was introduced bcz python used garbage collection to handle automatic memory allocation and deallocation. 

    1. **Reference counting**: Python uses reference counting to manage memory. Each object keeps track of how many references point to it. When the reference count drops to zero i.e., no references remain, Python automatically deallocates the object. For cyclic references i.e. references pointing to each other this doesn't work for that we've garbage collection.

    2. **Garbage Collection**: Garbage collection is a memory management technique used in programming languages to automatically reclaim memory that is no longer accessible or in use by the application. This is able to detect and clean up objects involved in reference cycles.

- **matplotlib.pyplot & seaborn:**

    - Seaborn is basically just a wrapper around matplotlib. This makes the diagram look more polished.

    - Learned how to plot bar graph(horizontal and vertical), pie chart, histogram, scatter plot, boxplot. 


---

**Date:** 8-12 Jun, 2026