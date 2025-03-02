name = input("What is your name?")

match name:
    case "harry" | "herion" | "ron":
        print("hello")
    case "draco":
        print("slytherin")
    case _: #default
        print("who?")