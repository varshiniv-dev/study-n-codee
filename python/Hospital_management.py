#Create a Hospital Management Model using classes: Patient, Doctor, Appointment. Demonstrate constructor, inheritance, polymorphism
class Patient:
    def __init__(self, name, age):
        self.patient_name = name
        self.patient_age = age

    def display_details(self):
        return f"Patient: {self.patient_name}, Age: {self.patient_age}"


class Doctor:
    def __init__(self, name, specialty):
        self.doctor_name = name
        self.specialty = specialty

    def display_details(self):
        return f"Doctor: {self.doctor_name}, Specialty: {self.specialty}"


class Appointment(Patient, Doctor):
    def __init__(self, p_name, p_age, d_name, d_specialty, date):
        Patient.__init__(self, p_name, p_age)
        Doctor.__init__(self, d_name, d_specialty)
        self.date = date

    def display_details(self):
        return (
            f"{Patient.display_details(self)}, "
            f"{Doctor.display_details(self)}, "
            f"Date: {self.date}"
        )


app = Appointment("John Doe", 30, "Dr. Smith", "Cardiology", "2023-10-15")
print(app.display_details())
app = Appointment("Jane Roe", 25, "Dr. Adams", "Neurology", "2023-11-20")
print(app.display_details())
app = Appointment("Alice Brown", 40, "Dr. Clark", "Orthopedics", "2023-12-05")
print(app.display_details())
