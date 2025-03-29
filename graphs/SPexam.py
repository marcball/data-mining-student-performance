# Scatter plot of exam scores by gender
# Not using this scatter plot.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

# Create a scatter plot for math scores
plt.figure(figsize=(10, 8))
plt.scatter(df[df['gender'] == 'male']['math score'], df[df['gender'] == 'male']['reading score'], color='blue', label='Male', alpha=0.5)
plt.scatter(df[df['gender'] == 'female']['math score'], df[df['gender'] == 'female']['reading score'], color='red', label='Female', alpha=0.5)

# Add scatter plot for writing scores
plt.scatter(df[df['gender'] == 'male']['math score'], df[df['gender'] == 'male']['writing score'], color='green', label=None, alpha=0.5)
plt.scatter(df[df['gender'] == 'female']['math score'], df[df['gender'] == 'female']['writing score'], color='orange', label=None, alpha=0.5)

# Add labels and title
plt.xlabel('Math Score')
plt.ylabel('Exam Score')
plt.title('Scatter Plot of Exam Scores by Gender')

plt.legend(['Male (Reading)', 'Female (Reading)', 'Male (Writing)', 'Female (Writing)'])
plt.grid(True)
plt.show()
