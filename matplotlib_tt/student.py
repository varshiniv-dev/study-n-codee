# write a program in 9th block to show performance strength and across students
import matplotlib.pyplot as plt
import pandas as pd
data = {'student': ['student1', 'student2', 'student3'],
        'maths': [85, 90, 78],
        'science': [88, 92, 80],
        'english': [82, 89, 75],
        'study_hours': [5, 6, 4]}
df = pd.DataFrame(data)
print(df)
df = pd.DataFrame({
    "student": ["student1", "student2", "student3"],
    "maths": [85, 90, 78],
    "science": [88, 92, 80],
    "english": [82, 89, 75],
    "study_hours": [5, 6, 4]
})

plt.plot(df["student"], df["maths"])
plt.plot(df["student"], df["science"])
plt.plot(df["student"], df["english"])
plt.xlabel("Students")
plt.ylabel("marks")
plt.title("student marks trend")
plt.legend(["maths", "science", "english"])
plt.show()
