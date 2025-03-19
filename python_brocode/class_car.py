
class Car:
    # define class variable
    #constructor (similar to fun it has parameter)  #__ dunder(double underscore)
    def __init__(self, model, year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You can drive the car {self.model}")

    def stop(self):
        print(f"You can stop the car {self.model}")

    def describe(self):
        print(f"This is Model {self.model} and make year is {self.year}")