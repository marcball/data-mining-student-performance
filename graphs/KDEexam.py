# Kernel Density Estimation of Exam Scores
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("StudentsPerformance.csv")

# Create a figure and axes for the subplots
plt.figure(figsize=(10, 6))

# Plot KDE plots for math, reading, and writing scores
sns.kdeplot(df['math score'], label='Math Score', fill=True)
sns.kdeplot(df['reading score'], label='Reading Score', fill=True)
sns.kdeplot(df['writing score'], label='Writing Score', fill=True)

# Add title and labels
plt.title('Kernel Density Estimation (KDE) Plot of Exam Scores')
plt.xlabel('Score')
plt.ylabel('Density')

plt.legend()
plt.show()
