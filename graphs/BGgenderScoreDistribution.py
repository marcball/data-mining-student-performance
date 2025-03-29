import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')

melted_df = df.melt(id_vars='gender', value_vars=['math score', 'reading score', 'writing score'], var_name='Score Type', value_name='Score')

plt.figure(figsize=(12, 6))
sns.boxplot(x='Score Type', y='Score', hue='gender', data=melted_df, palette='pastel')

plt.title('Comparison of Score Distributions by Gender')
plt.xlabel('Score Type')
plt.ylabel('Score')
plt.legend(title='Gender')

# For READ.ME documentation.
plt.savefig("./score_distribution_by_gender.png")

plt.show()
