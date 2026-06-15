# Length using match case

# numbers = [1, 2, 3]
numbers = (1, 2, 3)

match numbers:
    case [x]:
        print("One item")

    case [x, y]:
        print("Two items")

    case [x, y, z]:
        print("Three items")