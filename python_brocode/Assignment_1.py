# 1. Create a List with values 2,4,6,8,10.
#    Find the sum of values in the list.
#    Implement using the below approaches:-
#     a. Using 'for' loop. Use a variable 'total'.
#     b. Use a built in python fuction to achieve it.
#     c. Create a function definition calculate_total(n)
#       Repurpose the logic in step_a.
# 	  Return the calculated total from the function.
# 	  Example:
# 		calculate_total([2,4,6,8,10])
# 		Answer: 30
# 	d. Implement using list comprehension.
# 	e. Implement using a lambda function and reduce()

# Create a List
nums= [2,4,6,8,10]
# a.Find Sum of the list: for loop
total = 0
for x in nums:
    total += x
print(total)

# b.Find Sum of the list: with build method
print(sum(nums))

# c.Find Sum of the list: Function
def calculate_total(num_list):
    total = 0
    for n in num_list:
        total += n
    return total
print(calculate_total(nums))

# d.Find Sum of the list method: list comprehension.
#[expression for item in iterable]
(print(sum([n for n in nums])))  # [n for n in nums] create a new list and just use sum method on this list

# e.Find Sum of the list: using a lambda function and reduce()
# reduce(fun,itertable)
# reduce (lambda arguments: expression, itertable)

from functools import reduce
result = reduce(lambda a,b: a+b, nums)
print(result)


