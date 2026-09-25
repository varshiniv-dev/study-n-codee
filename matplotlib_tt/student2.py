# write a program to display a bar chart to compare subject wise marks
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'student': ['Alice', 'Bob', 'Charlie', 'David'],
    'maths': [85, 78, 92, 88],
    'science': [92, 85, 88, 90],
    'english': [78, 92, 85, 80],
    'history': [88, 75, 90, 85],
    'geography': [90, 80, 92, 75]
}

df = pd.DataFrame(data)

df.set_index('student').plot(kind='bar')
marks = df.loc[1, ['maths', 'science', 'english']]
labels = ['maths', 'science', 'english']
plt.pie(marks, labels=labels, autopct='%1.1f%%')
plt.title('Marks Distribution')
plt.title('Subject-wise Marks Comparison')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()
