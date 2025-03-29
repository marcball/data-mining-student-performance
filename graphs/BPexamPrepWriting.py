# Boxplot of Test preparation course completion and Writing scores
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

# Plot box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='test preparation course', y='writing score', data=df)
plt.title('Box Plot of Writing Scores by Test Preparation Course Completion')
plt.xlabel('Test Preparation Course Completion')
plt.ylabel('Writing Score')
plt.grid(axis='y')
plt.show()
