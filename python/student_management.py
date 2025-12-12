#Student Management System. Create a Student class with name, roll, marks. Add methods: display(), grade(). Accept details for 5 students and:
#1.	Display all
#2.	Find highest marks
#3.	Display topper details
class student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        return f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}"

    def grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'


students = []
for i in range(5):
    name = input("Enter student name: ")
    roll = int(input("Enter student roll number: "))
    marks = float(input("Enter student marks: "))
    students.append(student(name, roll, marks))
print("\nStudent Details:")
for s in students:
    print(s.display(), "Grade:", s.grade())
highest_marks = max(students, key=lambda s: s.marks)
print("\nTopper Details:")
print(highest_marks.display(), "Grade:", highest_marks.grade())
