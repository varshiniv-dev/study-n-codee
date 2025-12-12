class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def display_info(self):
        return f"Name: {self.name}, ID: {self.student_id}"


class Attendance(Student):
    def __init__(self, name, student_id, date, status):
        super().__init__(name, student_id)
        self.date = date
        self.status = status

    def display_attendance(self):
        student_info = self.display_info()
        return f"{student_info}, Date: {self.date}, Status: {self.status}"


student1 = Attendance("Aiden", "S12345", "2023-10-01", "Present")
print(student1.display_attendance())
student2 = Attendance("Leila", "S67890", "2023-10-02", "Absent")
print(student2.display_attendance())
added_attendance = []


def add_attendance(attendance):
    added_attendance.append(attendance)


def update_attendance(student_id, date, new_status):
    for attendance in added_attendance:
        if attendance.student_id == student_id and attendance.date == date:
            attendance.status = new_status
            return f"Attendance updated for {attendance.name} on {date} to {new_status}"
    return "Attendance record not found."


def display_all_attendance():
    for attendance in added_attendance:
        print(attendance.display_attendance())


add_attendance(student1)
add_attendance(student2)
print(update_attendance("S67890", "2023-10-01", "Present"))
display_all_attendance()
