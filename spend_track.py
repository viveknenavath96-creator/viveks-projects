import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 3: Read the expense CSV file
df = pd.read_csv("expense.csv")

# Step 4: Display the first few rows
print("First few rows:")
print(df.head())

# Step 5: Check for missing values
print("\nMissing values:")
print(df.isna().sum())

# Step 6: Check and remove duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

# Step 7: Convert date column into date format
df["date"] = pd.to_datetime(df["date"])

print("\nDate column:")
print(df["date"])

# Step 8: Calculate total spending
total_amount = df["amount"].sum()

print("\nTotal Spending:", total_amount)

# Step 9: Find highest expense
print("\nHighest expense:",df["amount"].max())

# Step 10: Group by category "How much money did I spend on each category?" 
category_total=df.groupby("category")["amount"].sum()
print("\nGroup category:", category_total)

# Step 11: Sort category totals 
category_total = category_total.sort_values(ascending=False)
print("\nCategory total:",category_total)

# Step 12: Group by payment method
payment_group = df.groupby("payment_method")["amount"].sum()
print("\nPayment method:", payment_group)

# Step 13: Create month column
df["month"] = df["date"].dt.month
print(df)

# Step 14: Calculate monthly spending
calculate_monthly = df.groupby("month")["amount"].sum()
print(calculate_monthly)

# Step 15: Save category-wise spending to a CSV file
print(category_total.to_csv("category_total.csv"))

# Step 16: Create a bar chart
plt.figure()
plt.bar(category_total.index,category_total.values)
plt.xlabel("category")
plt.ylabel("Total Spending")
plt.title("Spending by Category")
#plt.show()

# Step 17: Create a line chart
plt.figure()
plt.plot(calculate_monthly.index,calculate_monthly.values)
plt.xlabel("Months")
plt.ylabel("Spending")
plt.title("Monthly Spending")
plt.show()

# Step 18: Display
print("\nTotal Spending:", total_amount)
print("\nHighest expense:",df["amount"].max())
print("\nGroup category:", category_total)
print("\nPayment method:", payment_group)
print("\nMonthly Spending:", calculate_monthly)