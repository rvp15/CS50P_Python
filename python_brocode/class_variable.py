# class variable = is shared among all instance of a class
#                     Defined outside the constructor
#                     Allow you to share data among all object created from that class

class Student:
    # class variables
    graduating_year = 2010
    number_of_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.number_of_students +=1

student1 = Student("Sponge Bob", 30)
student2 = Student("Patrick", 36)
student3 = Student("Sam", 32)

print(f"Name:{student1.name}, Age:{student1.age}, Graduating year: {Student.graduating_year}")
print(f"Total number of Students:{Student.number_of_students}")
