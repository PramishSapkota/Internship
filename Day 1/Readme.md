# Day 1 - Internship Journey

## Overview
Day 1 of my internship experience, focusing on basic and  foundational concepts of python.

## Topics Covered
- Python's nature(Complier or Intrepreter)
- Abstract Syntax Tree(AST)

## Key Learnings
- I used to think that python is a intrepreter but turns out it is the both a compiler and an intrepreter. Python codes are first compiled into bytecodes(.pyc file) and intrepreted by Python Virtual Machine(PVM) into machine code.

- Next i learned about AST, the python code is firstly tokenized then it is parsed by a parser to check for syntax correctness after that an AST is constructed, AST can detect errors that the parser cannot detect. Finally if all is well the bytecode is compiled.

-Python exposes AST using built in ast module.

## Notes
python -m py_compile filename.py

only makes the '.cpython' file while  

python -m filename

makes and execute the '.cpython' file.

## Resources
- (https://youtu.be/AisW8ZhqUuc)
- [AST](https://youtu.be/wINY109MG10)

---

**Date:** May 11, 2026