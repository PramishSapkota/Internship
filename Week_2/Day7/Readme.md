# Day 7 - Internship Journey

## Overview
Day 7 of my internship, focused on the functools module

## Topics Covered
- partial 
- partialmethod
- lru_cache
- wraps
- update_wrapper
- cmp_to_key
- reduce
- total_ordering
- singledispatch

## Key Learnings
- **partial and partialmethod** are used to fix certain arguments of a function and create a new function with fewer parameters. partial method is used for class methods while i also used partial with class method by some name mangling.

- **lru_cache** is used to cache the function result so the same function doesnt have to run again for the same arguments.

- **wraps** is used to get the metadata of the wrapped function nwhich is lost otherwise.

- **update_wrapper** is used to copy the metadata or attributes attributes (\_\_name__, \_\_doc__, etc.)

- **cmp_to_key** is used to convert a comparision function into a key function.

- **reduce** is used to aggregrate the result from the iterables. 

- **total_ordering** is used to automatically fill in the missing comparision methods. Equal to and another comparision method should be given. 

- **singledispatch** It enables type-based function overloading

 

## Resources
- [functools](https://www.geeksforgeeks.org/python/functools-module-in-python/)


---

**Date:** May 19, 2026  