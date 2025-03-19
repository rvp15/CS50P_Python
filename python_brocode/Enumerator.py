# The enumerate() function in Python is used to iterate over an iterable
# (like a list, tuple, or string) while keeping track of the index of each item.
####################################################################################
# enumerate(iterable, start=0)
####################################################################################

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

####################################################################################
 # Using enumerate() with Tuples

####################################################################################
students = (("John",59), ("Alice",56),( "Bob", 66))

for i,(name,score) in enumerate(students):
    print(f"Student {i}:{name} {score}")

print(sum(score for (name,score) in students))
####################################################################################
 # Using enumerate() with Filter
####################################################################################
items = ["apple", "banana", "cherry", "date"]

filtered = [(i,fruit) for i,fruit in enumerate(fruits) if "a" in fruit]
print(filtered)