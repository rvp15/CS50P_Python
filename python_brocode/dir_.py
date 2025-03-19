# Namespace in Python
# A namespace in Python is a system that ensures unique names for variables, functions, objects, and modules
# to avoid naming conflicts. It maps names (identifiers) to objects (values).

# Global namespace which is Available throughout the module

# dir(object)	Lists all attributes and methods of an object
#dir() (no arguments)	Lists all variables in the current scope
################################################################################
# on custom created class
class Employee:
    def __init__(self):
        print("Inside the constructor")

    def display_emp_details(self):
        pass

print(dir(Employee))  # Lists methods & attributes ofb Employee
################################################################################
# on inbuilt data types
s ="hello"
print(dir(s)) # Lists all string methods
################################################################################
lst = [1, 2, 3]
print(dir(lst))  # Lists all list methods
################################################################################
################################################################################

