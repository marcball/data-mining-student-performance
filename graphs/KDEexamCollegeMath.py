# Kernel Density Estimation of College levels and Math score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

# Create a KDE plot for math scores
plt.figure(figsize=(10, 8))
sns.kdeplot(df[df['parental level of education'] == "some high school"]['math score'], label="Some High School", fill=True)
sns.kdeplot(df[df['parental level of education'] == "high school"]['math score'], label="High School", fill=True)
sns.kdeplot(df[df['parental level of education'] == "some college"]['math score'], label="Some College", fill=True)
sns.kdeplot(df[df['parental level of education'] == "associate's degree"]['math score'], label="Associate's Degree", fill=True)
sns.kdeplot(df[df['parental level of education'] == "bachelor's degree"]['math score'], label="Bachelor's Degree", fill=True)
sns.kdeplot(df[df['parental level of education'] == "master's degree"]['math score'], label="Master's Degree", fill=True)

# Add labels and title
plt.xlabel('Math Score')
plt.ylabel('Density')
plt.title('Kernel Density Estimation (KDE) Plot of Math Scores by Parental Level of Education')

plt.legend()
plt.grid(True)
plt.show()
