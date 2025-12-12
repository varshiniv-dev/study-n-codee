class Person:
    def introduce(self):
        return "Hello, I am a person."


class Student(Person):
    def study(self):
        return "I am studying."


class CollegeStudent(Student):
    def attend_college(self):
        return "I am attending college."


college_student = CollegeStudent()
print(college_student.introduce())
print(college_student.study())
print(college_student.attend_college())
