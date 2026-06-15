# test.py

import sys

def main():

    print("__name__ =", __name__)
    print("__package__ =", __package__)
    print("argv[0] =", sys.argv[0])

if __name__ == "__main__":
    main()

# '''
# >>> python -m test
# __name__ = __main__
# __package__ = 
# argv[0] = ...\Internship\Week_5\test.py

# >>> python test.py
# __name__ = __main__
# __package__ = None
# argv[0] = test.py

# '''