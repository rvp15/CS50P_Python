def greet(*names):
    print(names) # collected in tuples ('John', 'Alice', 'Bob')
    for name in names:
        print(f"Hello, {name}!")

greet("John", "Alice", "Bob")
# Output:
# Hello, John!
# Hello, Alice!
# Hello, Bob!

#############################
def greet(**person_info):
    for key, value in person_info.items():
        print(f"{key}: {value}")

greet(first_name="John", last_name="Doe", age=30, test = "test_arg")
# Output:
# first_name: John
# last_name: Doe
# age: 30
