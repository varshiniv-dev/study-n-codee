def full_name(first, last):
    return first + " " + last


def get_attendance(total, attended):
    if total == 0:
        return 0
    return (attended / total) * 100


def eligibility(attendance_percentage):
    if attendance_percentage >= 75:
        return "Eligible"
    else:
        return "Not Eligible"
