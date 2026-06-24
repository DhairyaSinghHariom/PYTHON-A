choice = int(input("Enter choice (1-3): "))

match choice:
    case 1:
        print("You selected One")
    case 2:
        print("You selected Two")
    case 3:
        print("You selected Three")
    case _:
        print("Invalid Choice")
