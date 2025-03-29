# Kernel Density Estimation of College levels and Reading score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

# Create a KDE plot for reading scores
plt.figure(figsize=(10, 8))
sns.kdeplot(df[df['parental level of education'] == "some high school"]['reading score'], label="Some High School", fill=True)
sns.kdeplot(df[df['parental level of education'] == "high school"]['reading score'], label="High School", fill=True)
sns.kdeplot(df[df['parental level of education'] == "some college"]['reading score'], label="Some College", fill=True)
sns.kdeplot(df[df['parental level of education'] == "associate's degree"]['reading score'], label="Associate's Degree", fill=True)
sns.kdeplot(df[df['parental level of education'] == "bachelor's degree"]['reading score'], label="Bachelor's Degree", fill=True)
sns.kdeplot(df[df['parental level of education'] == "master's degree"]['reading score'], label="Master's Degree", fill=True)

# Add labels and title
plt.xlabel('Reading Score')
plt.ylabel('Density')
plt.title('Kernel Density Estimation (KDE) Plot of Reading Scores by Parental Level of Education')

plt.legend()
plt.grid(True)
plt.show()
