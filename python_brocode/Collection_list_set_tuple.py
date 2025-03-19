# Collections = single "Variable" used to store multiple values
# List =[] ordered and changeable. Duplicates allowed
# set = {} unordered and immutable, but Add/Remove ok. No duplicates
# Tuple = () ordered and unchangeable. Duplicates ok. FASTER

# List[]:

fruits = ["Apple", "Banana", "Cherry","Mango", "Papaya", "Pineapple"]
# print(help(fruits))

#length:
print(len(fruits))

#in operator: helps to find if a values is in this list
print("Apple" in fruits)

#append:
fruits.append("Kiwi")

#insert a value at a given index:
fruits.insert(0,"first_fruit_inserted")
#Remove
fruits.remove("first_fruit_inserted")

#return index of a value:
print(fruits.index("Banana"))

#Count a particular element in list
print(f"Count of apple:{fruits.count("Apple")}")

##############################################################################################################
                            # SETs{}: unordered, so no indexing ,immutable, NO duplicates, but can add/remove
                            # works well colors
##############################################################################################################

fruits_set = {"Apple", "Banana", "Cherry","Mango", "Papaya", "Pineapple"}
print("SETS")
#len:
print(len(fruits_set))

#in operator: helps to find if a values is in this list
print("Apple" in fruits_set)

#add:
fruits_set.add("Kiwi") # will be added anywhere

#remove:
fruits_set.remove("Kiwi")

#pop(): remove a random first fruit
fruits_set.pop()


for fru in fruits_set:
    print(fru)

    ##############################################################################################################
                        # Tuple(): ordered, unchangeable, has duplicates : FASTER
    ##############################################################################################################

fruits_tuple = ("Apple", "Banana", "Cherry", "Mango", "Papaya", "Pineapple")

#len:
print(len(fruits_tuple))

# in :
print("Apple" in fruits_tuple)

# return index of a value:
print(fruits_tuple.index("Banana"))

#Count a particular element in tuple
print(f"Count of apple:{fruits_tuple.count("Apple")}")