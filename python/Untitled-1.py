class product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def display_details(self):
        return f"ID: {self.id}, Name: {self.name}, Price: ${self.price:.2f}"


class electronics(product):
    def __init__(self, id, name, price, warranty):
        super().__init__(id, name, price)
        self.warranty = warranty

    def display_details(self):
        parent_details = super().display_details()
        return f"{parent_details}, Warranty: {self.warranty} years"


class clothing(product):
    def __init__(self, id, name, price, size):
        super().__init__(id, name, price)
        self.size = size

    def display_details(self):
        parent_details = super().display_details()
        return f"{parent_details}, Size: {self.size}"


my_electronic = electronics(101, "IPhone", 699.99, 2)
my_clothing = clothing(201, "Denim-jeans", 19.99, "XL")
print(my_electronic.display_details())
print(my_clothing.display_details())
