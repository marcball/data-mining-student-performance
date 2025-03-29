# Pie Charts of all variables (- exam scores)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

categorical_columns = ['gender', 'parental level of education', 'lunch', 'test preparation course']

# Create pie charts for each column
for column in categorical_columns:
    plt.figure(figsize=(8, 6))
    df[column].value_counts().plot.pie(autopct='%1.1f%%', startangle=140)
    plt.title(f'Distribution of {column}')
    plt.ylabel('')
    plt.show()
