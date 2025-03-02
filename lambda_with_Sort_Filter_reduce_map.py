
#1. sort with no lambda:
numbers = [5, 2, 8, 1, 3]
numbers.sort()  # Sorts in ascending order
print(numbers)  # Output: [1, 2, 3, 5, 8]


# 2. Sort with Lambda Function
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
# key is assigned to lambda function, as it returns student age to key,
#  key is then passed to sort function to compare and sort.
students.sort(key=lambda student: student[1])  # Sort by age, student[1] returnss age for each tuple
print(students)

########################## Sort(key =None, reverse=False)###############3
# key in sort argument, specifies a function to be applied to each list element before sorting(here lambda function just extract and gives)
# the fun will return a value that will be used for sorting

#3. Another Example
products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone", "price": 500},
    {"name": "Tablet", "price": 700}
]
# Sort products by price (ascending order)
products.sort(key = lambda product: product["price"])
print(products)

#4. Sorting in Descending Order: use the reverse=True parameter:

products.sort(key = lambda product: product["price"], reverse = True)
print(products)

#5.sort by string length
names = ["Alice", "Bob", "Charlie", "David"]
names.sort(key=len)  # Sort by string length
print(names)  # Output: ['Bob', 'Alice', 'David', 'Charlie']

##############################################################################################################
                            #Lambda with Filter Function : filter(function, iterable) 
############################################################################################################
#filter(function, iterable) => always returns filter object (called iterator), convert it into list/tuple/set
#1.
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
filtered = filter(lambda student: student[1] > 23, students)
print(list(filtered))

#2.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_even = filter(lambda number: number%2 == 0, numbers)
print(list(filtered_even))

##############################################################################################################
                            #Lambda with Reduce Function:  reduce(function, iterable)
############################################################################################################
#            reduce(function, iterable[, initializer])
#function === binary function(which takes 2 arguments)
from functools import reduce
#1.sum of a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = reduce(lambda x,y : x+y, numbers)
print(sum)

num1 = [1,2,3,4]
product = reduce(lambda x,y: x*y , num1)
print(f"product: {product}")

find_max = reduce(lambda x,y: max(x,y),num1 )
print(find_max)



##############################################################################################################
                            #Lambda with MAP Function:  map(function, iterable)
############################################################################################################
#map() applies a given function to all items in an iterable, and it works well with lambda functions.
#  For example, applying a function to square all numbers in a list:

numbers = [1, 2, 3, 4]
squared_numbers = map(lambda x: x ** 2, numbers)
# Convert the map object to a list and print
print(list(squared_numbers))  # Output: [1, 4, 9, 16]



##############################################################################################################
                            #Lambda with any() and all(): 
############################################################################################################
#any() and all() are built-in functions that can be used with lambda to check conditions across iterables.

#1.any() returns True if any element of the iterable is True:
numbers = [0, 2, 3, 4]

result = any(map(lambda x: x % 2 == 0, numbers))  # Check if any number is even
print(result)  # Output: True

#2.all() returns True only if all elements of the iterable are True:
numbers = [2, 4, 6, 8]

result = all(map(lambda x: x % 2 == 0, numbers))  # Check if all numbers are even
print(result)  # Output: True
