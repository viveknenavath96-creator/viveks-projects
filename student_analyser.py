# ==========================================
# STUDENT PERFORMANCE ANALYSIS
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the student dataset
data_frame = pd.read_csv("student_data.csv")


# ==========================================
# 2. DATASET EXPLORATION
# ==========================================

# Display the first 5 records
print(data_frame.head())

# Display the last 5 records
print(data_frame.tail())

# Display records from index 15 to 19
print(data_frame.iloc[15:20])

# Display the total number of rows and columns
print(data_frame.shape)

# Display column names and data types
print(data_frame.columns)
print(data_frame.dtypes)

# Display dataset information
data_frame.info()

# Identify missing values in each column
print(data_frame.isnull().sum())

# Generate basic statistical information
print(data_frame.describe())


# ==========================================
# 3. DATA CLEANING
# ==========================================

# Calculate the average Mathematics marks
Average = data_frame["math"].mean()
print(f"Average Mathematics marks: {Average}")

# Fill missing Mathematics values with the average
data_frame["math"] = data_frame["math"].fillna(Average)

# Calculate the average Science marks
science_avg = data_frame["science"].mean()
print(f"Average Science marks: {science_avg}")

# Fill missing Science values with the average
data_frame["science"] = data_frame["science"].fillna(science_avg)

# Calculate the average English marks
english_avg = data_frame["english"].mean()
print(f"Average English marks: {english_avg}")

# Fill missing English values with the average
data_frame["english"] = data_frame["english"].fillna(english_avg)

# Calculate the average attendance
attendance = data_frame["attendance"].mean()
print(f"Average attendance: {attendance}")

# Fill missing attendance values with the average
data_frame["attendance"] = data_frame["attendance"].fillna(attendance)

# Count duplicate records
print("Duplicate records:", data_frame.duplicated().sum())

# Remove duplicate records
data_frame = data_frame.drop_duplicates()

# Verify missing values after cleaning
print("\nMissing values after cleaning:")
print(data_frame.isnull().sum())

# Verify duplicate records after cleaning
print("\nDuplicates after cleaning:")
print(data_frame.duplicated().sum())


# ==========================================
# 4. STUDENT MARKS CALCULATION
# ==========================================

# Calculate total marks for each student
data_frame["Total_marks"] = data_frame[["math", "science", "english"]].sum(axis=1)

# Calculate average marks for each student
data_frame["Average_marks"] = data_frame[["math", "science", "english"]].mean(axis=1)

# Determine whether each student passed or failed
# A student passes only if all three subject marks are at least 35
data_frame["Result"] = (
    data_frame[["math", "science", "english"]]
    .apply(lambda row: "Pass" if all(row >= 35) else "Fail", axis=1)
)


# ==========================================
# 5. TOP STUDENTS ANALYSIS
# ==========================================

# Sort students based on average marks in descending order
top_students = data_frame.sort_values(by="Average_marks", ascending=False)

# Display the top 5 students
print("\nTop 5 Students:")
print(top_students[["name", "Average_marks"]].head(5))


# ==========================================
# 6. SUBJECT-WISE ANALYSIS
# ==========================================

# Calculate average marks for each subject
subject_wise_average_marks = data_frame[["math", "science", "english"]].mean()

# Display average marks for each subject
print("\nSubject-wise Average Marks:")
print(subject_wise_average_marks)


# ==========================================
# 7. DATA VISUALIZATION
# ==========================================

# 7.1 Display average marks for each subject using a bar chart
plt.figure(figsize=(8, 5))
plt.bar(subject_wise_average_marks.index, subject_wise_average_marks.values)
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.show()

# 7.2 Display each student's average marks using a bar chart
plt.figure(figsize=(10, 6))
plt.bar(data_frame["name"], data_frame["Average_marks"])
plt.title("Student Performance Analysis")
plt.xlabel("Student Names")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.show()

# 7.3 Display the distribution of student average marks using a histogram
plt.figure(figsize=(8, 5))
plt.hist(data_frame["Average_marks"], color="red")
plt.title("Distribution of Student Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.show()

# 7.4 Compare average performance by gender using a bar chart
gender_wise_performance = data_frame.groupby("gender")["Average_marks"].mean()

plt.figure(figsize=(8, 5))
plt.bar(gender_wise_performance.index, gender_wise_performance.values)
plt.title("Gender-wise Average Performance")
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.show()


# ==========================================
# 8. PERFORMANCE ANALYSIS
# ==========================================

# Identify the highest-scoring student in each subject
print("\nHighest-scoring student index in each subject:")
print(data_frame[["math", "science", "english"]].idxmax())

# Identify the student with the highest average marks
print("\nHighest-performing student:")
print(data_frame.loc[data_frame["Average_marks"].idxmax(), "name"])

# Identify the student with the lowest average marks
print("\nLowest-performing student:")
print(data_frame.loc[data_frame["Average_marks"].idxmin(), "name"])

# Count the number of students who passed and failed
print("\nPass/Fail Count:")
print(data_frame["Result"].value_counts())

# Calculate the overall class average
print("\nOverall Class Average:")
print(data_frame["Average_marks"].mean())


# ==========================================
# 9. FINAL STUDENT PERFORMANCE REPORT
# ==========================================

print("\n===== STUDENT PERFORMANCE REPORT =====")

# Display the total number of students
print("Total Students:", len(data_frame))

# Display the overall class average
print("Class Average:", round(data_frame["Average_marks"].mean(), 2))

# Display the pass and fail count
print("\nPass/Fail Count:")
print(data_frame["Result"].value_counts())

# Display the highest-performing student
print("\nHighest Performing Student:")
print(data_frame.loc[data_frame["Average_marks"].idxmax(), "name"])

# Display the lowest-performing student
print("\nLowest Performing Student:")
print(data_frame.loc[data_frame["Average_marks"].idxmin(), "name"])


# ==========================================
# 10. SAVE THE UPDATED DATASET
# ==========================================

# Save the cleaned dataset with calculated columns to a new CSV file
data_frame.to_csv("student_updated.csv", index=False)

print("\nUpdated student dataset saved successfully!")