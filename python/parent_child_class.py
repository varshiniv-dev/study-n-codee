#Create a parent class Vehicle and a child class Car. Use constructor in both classes. Use super() to call parent constructor. Add a method to display details.
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_details(self):
        return f"Vehicle Make: {self.make}, Model: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def display_details(self):
        parent_details = super().display_details()
        return f"{parent_details}, Year: {self.year}"


my_car1 = Car("Porsche", "911", 2023)
my_car2 = Car("BMW", "M5", 2025)
my_car3 = Car("Audi", "R8", 2024)
my_car4 = Car("Mercedes", "C-Class", 2022)
print(my_car1.display_details())
print(my_car2.display_details())
print(my_car3.display_details())
print(my_car4.display_details())
print(my_car1.make)
print(my_car2.model)
print(my_car3.year)
print(my_car4.make)
