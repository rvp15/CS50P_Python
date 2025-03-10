# Python allows you to gracefully handle runtime errors  instead of crashing program

#################################################################################
                 # try-expect Block
#################################################################################


# try: 
#     total_salary = int(input("Enter the total salary:"))
#     no_emp = int(input("Enter number of employees ").strip())
#     avg_salary = total_salary/no_emp
#     print(avg_salary)
# except ZeroDivisionError:
#     print("Error: number of employee cant be zero")
# except ValueError:  # Handles invalid input (e.g., entering a letter instead of a number or no input entered)
#   print("Error: Please provide valid input")

  
#################################################################################
                 # try-expect Block   with while 
#############################################################################

# while True:  # Keep asking until valid input is provided
#     try:
#         no_emp = int(input("Enter number of employees: ").strip())  # Strip removes accidental spaces
#         total_salary = int(input("Enter the total salary:"))
#         avg_salary = total_salary/no_emp
#         print(avg_salary)
#         break  # Exit the loop if input is valid
#     except ValueError:
#         print("Invalid input! Please enter a valid integer.")
#     except ZeroDivisionError:
#         print("Error: number of employee cant be zero")

####################################################################################
        #2. Handling Multiple Exceptions
####################################################################################
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("Result:", result)
# except (ZeroDivisionError, ValueError) as e:  # Catch multiple errors
#     print(f"Error occurred: {e}")

####################################################################################
        #3.  Using else Block
####################################################################################
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
   
# except (ZeroDivisionError, ValueError) as e:  # Catch multiple errors
#     print(f"Error occurred: {e}")
# else:                                           # Else block execute when there is no exception
#      print("Success! Result:", result)

#######################################################################################
        #4. Using finally Block
#######################################################################################
try:
    num = int(input("Enter a number: "))
    result = 10 / num
   
except (ZeroDivisionError, ValueError) as e:  # Catch multiple errors
    print(f"Error occurred: {e}")
finally:                                          
     print("This line executes at all time")