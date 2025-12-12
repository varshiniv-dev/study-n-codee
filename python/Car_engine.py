# Create a program using composition:, Class Engine, Class Car containing Engine object, Show how both classes interact
class Engine:
    def __init__(self, horsepower, engine_type):
        self.horsepower = horsepower
        self.engine_type = engine_type

    def display_specs(self):
        return f"{self.horsepower} HP, Type: {self.engine_type}"


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.engine = Engine(300, "V6")

    def display_details(self):
        parent_details = f"Make: {self.make}, Model: {self.model}, Engine Specs: {self.engine.display_specs()}"
        return f"{parent_details}, Year: {self.year}"


my_car1 = Car("Porsche", "911", 2023)
my_car2 = Car("BMW", "M5", 2025)
my_car3 = Car("Audi", "R8", 2024)
my_car4 = Car("Mercedes", "C-Class", 2022)
my_car5 = Car("Tesla", "Model S", 2023)
print(my_car1.display_details())
print(my_car2.display_details())
print(my_car3.display_details())
print(my_car4.display_details())
print(my_car5.display_details())
print(my_car1.make)
print(my_car2.model)
print(my_car3.year)
print(my_car4.make)
print(my_car5.engine.display_specs())
