# Reading vs. Writing scatter plot
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')

plt.figure(figsize=(10, 6))
sns.scatterplot(x='reading score', y='writing score', data=df, alpha=0.6, edgecolor='w')

plt.title('Reading Score vs. Writing Score')
plt.xlabel('Reading Score')
plt.ylabel('Writing Score')
plt.grid(True)
plt.show()
