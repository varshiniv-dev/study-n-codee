import studentutils as su
first = "Kim"
last = "Mingyu"
total_classes = 60
attended_classes = 48
name = su.full_name(first, last)
attendance_percentage = su.get_attendance(total_classes, attended_classes)
status = su.eligibility(attendance_percentage)
print("Full Name:", name)
print("Attendance Percentage:", attendance_percentage)
print("Eligibility:", status)
