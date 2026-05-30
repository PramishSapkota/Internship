# Library Management System(LMS)

## Overview
This is a simple simulation of  Library Management System using python 

## Concepts Used
- File Handling(CSV files)
- OOP

## Key Learnings and Notes
- Learned about abstract methods:

  Abstract methods are the methods that have to be defined in child classes. To make an Abstract method we need to import the abstractmethod method from abc module and the class should also be a child class of class ABC.

- Learned about *@property* decorators:

    These decorators allows us to define getter, setter, and deleter methods for an attribute while accessing it via standard dot notation (e.g., obj.attr instead of obj.get_attr()).

    - Previously i had only learned about them but i got hands-on-experience about them through this project. Also, using property decorator,we can access the method as we would access an attribute i.e without using the small bracket'()'. This made the code more pythonic

- Learned about *datetime* module

  Used the datetime module to handle date operations. mainly strftime, strptime and timedelta. 
  strftime converts the datetime into string format to store and strptime is used to convert string into datetime. Finally timedelta was used to add 14 days to the issuedate.

-  Learned about os.makedirs and os.path.dirname:
  <!-- ```
  os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
  ``` -->

  *os.makedirs* is used to create folders recursively, if they dont exist. *os.path.dirname* extracts the directory portion of the file path, excluding the filename. *exist_ok=True* prevents a FileExistsError from being raised if the target directory (or any intermediate directory) already exists.

- Learned that while initializing objects its best to use keyword arguments. This makes the code more robust

  I learned this the hard way. Before, assigning the id was manual but later i made that automatic for that i had to set the id field parameter as None and keep it as last parameter bcz the default parameter should be behind the non default ones. 
  Doing so, resulted in the wrong parameter assignment to objects and ultimately the file also had saved wrong fields .

- Learned some pythonic techniques using which i can do some tasks in a single line which would have otherwise taken me multilines and creating a function and calling it.

- Learned that we can print dashes or other symbols as many times we want using **f"{'--'\*25}"** instead of manually



---

**Date:** May 29, 2026