language = input("Enter a programming language: ")
language = language.lower()


match language:

    case "python":
        print("I Know about Python")

    case "java":
        print("I Know about Java")

    case "javascript":
        print("I Know about Javascript")

    case "c++":
        print("I Know about C++")

    case "c":
        print("I Know about C")

    case "c#":
        print("I Know about C#")

    case "r":
        print("I Know about R")

    case _:
        print("Unknown language detected")
