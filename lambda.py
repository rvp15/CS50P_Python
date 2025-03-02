#syntax: Lambda Functions are Anonymous
#They are used for short-lived, one-time-use functions.Can have multiple arguments , but single expression to calculate it. 
#1.Syntax:
# ############# lambda arguments: expression #####################
add = lambda a, b: a + b
print(add(2, 4))

#2. call a lambda function immediately without assigning it to a variable.
#  This is called an immediately invoked lambda expression (IILE).

print((lambda a,b: a+b) (4,4))

#3. (IILE) without arguments by defining a lambda function with no parameters
print((lambda: "Hello, Lambda!")())  
# Output: Hello, Lambda!

#4. Lambda + MAP:

####### map(function, iterable)
#1. with normal function:
def square(n):
    return n*n

nums = [3,6,4,9,5]
 # nums is iterable, each num is taken and given to square fun
 # This is higher order function, as a fun(square) is passed to another fun (map)
squared_nums = list(map(square, nums))
print(squared_nums)

#2. Map with Lambda:
squared =list(map(lambda x: x*x,nums))
print(squared)

#. Map with Multiple Iteratable:
a = [1, 2, 3]
b = [4, 5, 6]
#map (lambda fun, iteratable)
list_sum = list(map(lambda x,y: x+y, a,b))
print(list_sum)

########################################################################################################

#Lambda with filter()