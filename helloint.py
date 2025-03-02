# int = whole number -, + but not decimal
# to run python interactive mode, in terminal type python and enter => you can start interactive mode >>>

x = input("Value of x:") # input is a function which assign its value to left variable
y = input("Value of Y:")
z = int(x) + int(y)   # int is a function in python, which converts the arguments passed to it to integer
print(z)

#can aslo be written as  nested function:   inner fun is called first its result is given as argument to outer fun int

#FLOAT:

a = float(input("What is a:"))
b = float(input("What is b:"))
# round the decimal point:  round(number, ndigit)  => ndigit is optional perameter where you can spcify how many digit to round round(4.4643,2)=> 4.46 (2 digit after pont)
c= round(a+b)
print(c)
print(f"{c:,}")  # the larger number will be formatted here,a=999, b=1 c=1,000
""" 
The colon : inside {} specifies formatting instructions:
→ Adds thousands separators (comma for English locale).
 """
#Division 
d= round(a/b, 2)  #=> 2nd argument specifies how many decimal to be rounded 
print(d)
# another version to round up and specify number of interger

e =a/b
print(f"{e:.2f}") # after colon specify number of int to be rounded
