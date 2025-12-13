#Build a University Result Management System using: Base class Person. Derived class Student. Attributes: subject marks. Methods: calculate total, percentage, grade
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, subjects_marks):
        super().__init__(name, age)
        self.subjects_marks = subjects_marks  # Dictionary of subject: marks

    def calculate_total(self):
        return sum(self.subjects_marks.values())

    def calculate_percentage(self):
        total_marks = self.calculate_total()
        num_subjects = len(self.subjects_marks)
        # Assuming each subject is out of 100
        return (total_marks / (num_subjects * 100)) * 100

    def determine_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return 'A'
        elif percentage >= 80:
            return 'B'
        elif percentage >= 70:
            return 'C'
        elif percentage >= 60:
            return 'D'
        else:
            return 'F'


# Example usage
subjects_marks = {
    'Math': 95,
    'Science': 88,
    'History': 76,
    'English': 85
}
student1 = Student("Alice", 20, subjects_marks)
print(student1.display_info())
print("Total Marks:", student1.calculate_total())
print("Percentage:", student1.calculate_percentage())
print("Grade:", student1.determine_grade())
student2 = Student("Bob", 22, {
    'Math': 65,
    'Science': 70,
    'History': 72,
    'English': 68
})
print(student2.display_info())
print("Total Marks:", student2.calculate_total())
print("Percentage:", student2.calculate_percentage())
print("Grade:", student2.determine_grade())
student3 = Student("Charlie", 21, {
    'Math': 45,
    'Science': 55,
    'History': 60,
    'English': 50
})
print(student3.display_info())
print("Total Marks:", student3.calculate_total())
print("Percentage:", student3.calculate_percentage())
print("Grade:", student3.determine_grade())
student4 = Student("Diana", 23, {
    'Math': 85,
    'Science': 90,
    'History': 88,
    'English': 92
})
print(student4.display_info())
print("Total Marks:", student4.calculate_total())
print("Percentage:", student4.calculate_percentage())
print("Grade:", student4.determine_grade())
total_students = 4
print("Total Students Processed:", total_students)
student_names = [student1.name, student2.name, student3.name, student4.name]
print("Student Names:", student_names)
average_percentage = (student1.calculate_percentage() + student2.calculate_percentage() +
                      student3.calculate_percentage() + student4.calculate_percentage()) / total_students
print("Average Percentage:", average_percentage)
highest_scorer = max(
    [student1, student2, student3, student4],
    key=lambda s: s.calculate_total()
)
print("Highest Scorer:", highest_scorer.name,
      "with Total Marks:", highest_scorer.calculate_total())
lowest_scorer = min(
    [student1, student2, student3, student4],
    key=lambda s: s.calculate_total()
)
print("Lowest Scorer:", lowest_scorer.name,
      "with Total Marks:", lowest_scorer.calculate_total())
