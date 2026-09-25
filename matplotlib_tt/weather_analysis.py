# Program to display weather analysis using line, bar, and pie charts

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Sample weather data (temperature in Celsius for a week)
data = """
Day,Temperature
Monday,22
Tuesday,24
Wednesday,19
Thursday,23
Friday,25
Saturday,20
Sunday,21
"""

# Read data into DataFrame
df = pd.read_csv(StringIO(data))

# ---------- LINE CHART ----------
plt.figure(figsize=(10, 5))
plt.plot(df['Day'], df['Temperature'], marker='o')
plt.title('Weekly Temperature - Line Chart')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# ---------- BAR CHART ----------
plt.figure(figsize=(10, 5))
plt.bar(df['Day'], df['Temperature'])
plt.title('Weekly Temperature - Bar Chart')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.show()

# ---------- PIE CHART ----------
plt.figure(figsize=(8, 8))
plt.pie(df['Temperature'], labels=df['Day'], autopct='%1.1f%%')
plt.title('Weekly Temperature Distribution - Pie Chart')
plt.show()
# End of weather_analysis.py
