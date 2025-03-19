# Object = A bundle of related attributes (variables) and methods (functions)
#             Ex: phone, cup, book
#              1. (phone): attribute: color="red", price = 250,
#              2. method: make_call()  (method is a fun that belongs to object)
#
#               You need a "class" to create many objects (many phones with different attribute values maybe)

#class = (blueprint) used to design the structure and layout of an object
#
# class Car:
#     #constructor (similar to fun it has parameter)  #__ dunder(double underscore)
#     def __init__(self, model, year,color,for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

from class_car import Car

# 1.Create Object
car1 = Car("Mustang",2024,"red", False) # create object
car2= Car("Corvette",2023,"blue", True)

print(car1) # gives the memory address of the object created

#2. Access attribute:
print(car1.model)

# 3.Access method:
car2.drive()
car1.stop()
car1.describe()