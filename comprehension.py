#  comprehension is a concise way to create lists, dictionaries, and sets using a single line of code.

###################################################################################
                      #  List Comprehension
                    # [expression for item in iterable]
               # [expression for item in iterable if condition]
#####################################################################################

print([x*2 for x in range(5) if x%2==0])

fruits = ["apple", "banana", "cherry", "mango", "grape", "orange", "watermelon", "strawberry", "blueberry", "pineapple"]

print([fruit for fruit in fruits if fruit[0] in 'aeiou'])

print([fruit for fruit in fruits if len(fruit) == 5])

###################################################################################
                      #  Dictionary  Comprehension
    # {key_expression: value_expression for item in iterable if condition}
####################################################################################

original_dict = {'a': 1, 'b': 2, 'c': 3}
 #.items() is used to retrieve key-value pairs as tuples.
print(original_dict.items())   # helps to unpack both key and value together
# Output: dict_items([('a', 1), ('b', 2), ('c', 3)])
#It returns an iterable of tuples, where each tuple is (key, value).

print( { key:value*2 for key,value in original_dict.items() })

modified = {key : value *2 for key,value in original_dict.items() if value%2==0}
print(modified)

#2. Create a Dict mapping numbers to their squares
 # {key_expression: value_expression for item in iterable if condition}
print({x:x**2 for x in range(1,6)})

####################################################################################
 
####################################################################################