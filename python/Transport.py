# Create a Transport Booking System with:, Base class Vehicle, Derived classes Bus, Auto, Taxi, Include fare calculation method (polymorphism)
class Vehicle:
    def __init__(self, distance):
        self.distance = distance

    def calculate_fare(self):
        return 0


class Bus(Vehicle):
    def calculate_fare(self):
        return self.distance * 5


class Auto(Vehicle):
    def calculate_fare(self):
        return self.distance * 10


class Taxi(Vehicle):
    def calculate_fare(self):
        return self.distance * 15


bus_list = [Bus(10), Bus(20)]
auto_list = [Auto(10), Auto(15)]
taxi_list = [Taxi(10), Taxi(25)]
print("Bus Fares:")
for b in bus_list:
    print(b.calculate_fare())
print("\nAuto Fares:")
for a in auto_list:
    print(a.calculate_fare())
print("\nTaxi Fares:")
for t in taxi_list:
    print(t.calculate_fare())
