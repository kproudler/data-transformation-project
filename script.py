from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

print(financial_data.head())

month = financial_data.Month
revenue = financial_data.Revenue
expenses = financial_data.Expenses

# Examination of revenue and expenses over the past 6 months

plt.plot(month, revenue)
plt.xlabel('Month')
plt.title('Revenue')
plt.ylabel('Amount ($)')
plt.show()

plt.clf()
plt.plot(month, expenses)
plt.title('Expenses')
plt.xlabel('Expenses')
plt.ylabel('Amount ($)')
plt.show()

