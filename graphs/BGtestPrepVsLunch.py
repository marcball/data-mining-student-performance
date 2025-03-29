# Test Preperation Course Completion by Lunch Type Bar Graph
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')

# contingency table
lunch_prep = pd.crosstab(df['lunch'], df['test preparation course'])

lunch_prep_percentage = lunch_prep.div(lunch_prep.sum(1), axis=0)


lunch_prep_percentage.plot(kind='bar', stacked=True, color=['#1f77b4', '#ff7f0e'])
plt.title('Test Preparation Course Completion by Lunch Type')
plt.xlabel('Lunch Type')
plt.ylabel('Percentage')
plt.legend(title='Test Preparation Course', labels=['Not Completed', 'Completed'])
plt.xticks(rotation=0)  
plt.show()