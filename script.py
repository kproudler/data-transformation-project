from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

# print(financial_data.head())

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

expense_overview = pd.read_csv('expenses.csv')
# print(expenses_overview.head(7))

# expense_categories = expense_overview.Expense
# proportions = expense_overview.Proportion

expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]

# visualisation of expense categories and their proportions
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expenses')
plt.axis('Equal')
plt.tight_layout()
plt.show()

# Salaries make up the majority of expenses (62%) - might requires a cut

employees = pd.read_csv('employees.csv')
# print(employees.head())

sorted_productivity = employees.sort_values(['Productivity'])
# print(sorted_productivity)

# Salary expense effect of cutting the least 100 productive employees
employees_cut = sorted_productivity[0:100]
print(employees_cut.Salary.sum())

# commute times - skew of 1.1484
commute_times = employees['Commute Time']
# print(commute_times.skew())

# commute log - skew of -0.4241
commute_times_log = np.log(commute_times)
# print(commute_times.describe())
# print(commute_times_log.skew())

plt.clf()
plt.hist(commute_times_log)
plt.title('Commute Times')
plt.xlabel('Minutes')
plt.ylabel('Frequency')
plt.show()

# standardization of employee - productivity
salary_productivity = employees[['Salary', 'Productivity']].copy()
standardizer = preprocessing.StandardScaler()
scaled_salary = standardizer.fit_transform(salary_productivity)

# scaler = preprocessing.MinMaxScaler()
# scaled_salary = scaler.fit_transform(salary_productivity)

# Does not seem to be a relationship between Productivity and Salary
plt.clf()
plt.plot(scaled_salary, 'bo')
plt.xlabel('Salary')
plt.ylabel('Productivity')
plt.title('Standardized Income-Productivity')

plt.show()
