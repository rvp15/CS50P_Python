class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee name: {self.name} salary: {self.salary}"

    def __gt__(self, emp2):
        return self.salary > emp2.salary

emp1 = Employee("ve", 3000)
emp2 = Employee("bb", 6000)

print(emp1 > emp2)  # This will call the __gt__ method # emp1.__gt__(emp2)
