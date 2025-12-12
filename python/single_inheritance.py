class Animal:
    def eat(self):
        return "The animal is eating."


class Dog(Animal):
    def bark(self):
        return "The dog is barking."


dog = Dog()
print(dog.eat())
print(dog.bark())
