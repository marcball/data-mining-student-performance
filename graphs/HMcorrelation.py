# Heatmap Correlation
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')


correlation_matrix = df[['math score', 'reading score', 'writing score']].corr()

#matplotlib figure
plt.figure(figsize=(8, 6))

#draw heatmap with mask and correct aspect ratio
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=.5, cbar_kws={"shrink": .8})

#titles + labels
plt.title('Correlation Between Math, Reading, and Writing Scores')
plt.show()
