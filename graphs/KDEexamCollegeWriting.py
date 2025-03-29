# Kernel Density Estimation of College levels and Writing score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

# Create a KDE plot for writing scores
plt.figure(figsize=(10, 8))
sns.kdeplot(df[df['parental level of education'] == "some high school"]['writing score'], label="Some High School", fill=True)
sns.kdeplot(df[df['parental level of education'] == "high school"]['writing score'], label="High School", fill=True)
sns.kdeplot(df[df['parental level of education'] == "some college"]['writing score'], label="Some College", fill=True)
sns.kdeplot(df[df['parental level of education'] == "associate's degree"]['writing score'], label="Associate's Degree", fill=True)
sns.kdeplot(df[df['parental level of education'] == "bachelor's degree"]['writing score'], label="Bachelor's Degree", fill=True)
sns.kdeplot(df[df['parental level of education'] == "master's degree"]['writing score'], label="Master's Degree", fill=True)

# Add labels and title
plt.xlabel('Writing Score')
plt.ylabel('Density')
plt.title('Kernel Density Estimation (KDE) Plot of Writing Scores by Parental Level of Education')


plt.legend()
plt.grid(True)
plt.show()
