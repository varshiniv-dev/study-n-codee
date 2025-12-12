#Build a University Result Management System using: Base class Person. Derived class Student. Attributes: subject marks. Methods: calculate total, percentage, grade
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def grade(self):
        p = self.percentage()
        if p >= 90:
            return "A"
        elif p >= 80:
            return "B"
        elif p >= 70:
            return "C"
        elif p >= 60:
            return "D"
        else:
            return "F"


student1 = Student("Vansh", 20, [95, 88, 76, 85])
student2 = Student("Aryan", 22, [65, 70, 72, 68])
print("Name:", student1.name, "| Total:", student1.total(),
      "| %:", student1.percentage(), "| Grade:", student1.grade())
print("Name:", student2.name, "| Total:", student2.total(),
      "| %:", student2.percentage(), "| Grade:", student2.grade())
