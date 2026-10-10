import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the expense CSV file
df = pd.read_csv("expense.csv")

# Step 2: Display the first few rows
print("First few rows:")
print(df.head())

# Step 3: Check for missing values
print("\nMissing values:")
print(df.isna().sum())

# Step 4: Check and remove duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

# Step 5: Convert date column into date format
df["date"] = pd.to_datetime(df["date"])

print("\nDate column:")
print(df["date"])

# Step 6: Calculate total spending
total_amount = df["amount"].sum()
print("\nTotal Spending:", total_amount)

# Step 7: Find highest expense
print("\nHighest expense:",df["amount"].max())

# Step 8: Group by category "How much money did I spend on each category?" 
category_total=df.groupby("category")["amount"].sum()
print("\nGroup category:", category_total)

# Step 9: Sort category totals 
category_total = category_total.sort_values(ascending=False)
print("\nCategory total:",category_total)

# Step 10: Group by payment method
payment_group = df.groupby("payment_method")["amount"].sum()
print("\nPayment method:", payment_group)

# Step 11: Create month column
df["month"] = df["date"].dt.month
print(df)

# Step 12: Calculate monthly spending
calculate_monthly = df.groupby("month")["amount"].sum()
print(calculate_monthly)

# Step 13: Save category-wise spending to a CSV file
print(category_total.to_csv("category_total.csv"))

# Step 14: Create a bar chart
plt.figure()
plt.bar(category_total.index,category_total.values)
plt.xlabel("category")
plt.ylabel("Total Spending")
plt.title("Spending by Category")

# Step 15: Create a line chart
plt.figure()
plt.plot(calculate_monthly.index,calculate_monthly.values)
plt.xlabel("Months")
plt.ylabel("Spending")
plt.title("Monthly Spending")
plt.show()

# Step 16: Display
print("\nTotal Spending:", total_amount)
print("\nHighest expense:",df["amount"].max())
print("\nGroup category:", category_total)
print("\nPayment method:", payment_group)
print("\nMonthly Spending:", calculate_monthly)
