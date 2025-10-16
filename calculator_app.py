# 🎓 GPA & CGPA Calculator
# Author: Umm e Aatika (FA23-BST-078)
# Institution: COMSATS University Islamabad, Lahore Campus

import numpy as np
import pandas as pd

print("===================================")
print("      🎓 GPA & CGPA Calculator      ")
print("===================================")

# -------------------------------
# Step 1: GPA Calculation
# -------------------------------
num_courses = int(input("Enter number of subjects in this semester: "))

grades = []
credits = []

for i in range(num_courses):
    g = float(input(f"Enter grade points for subject {i+1} (e.g. 3.5): "))
    c = float(input(f"Enter credit hours for subject {i+1}: "))
    grades.append(g)
    credits.append(c)

grades = np.array(grades)
credits = np.array(credits)

gpa = np.sum(grades * credits) / np.sum(credits)
print("\n👉 Your GPA for this semester is:", round(gpa, 2))

# -------------------------------
# Step 2: CGPA Calculation
# -------------------------------
n = int(input("\nEnter number of semesters completed: "))
gpa_list = []

for i in range(n):
    g = float(input(f"Enter GPA for semester {i+1}: "))
    gpa_list.append(g)

cgpa = np.mean(gpa_list)

# -------------------------------
# Step 3: Show Summary using Pandas
# -------------------------------
data = {'Semester': [f'Sem {i+1}' for i in range(n)], 'GPA': gpa_list}
df = pd.DataFrame(data)

print("\n📘 GPA Summary Table:")
print(df)
print("\n🎯 Your Overall CGPA is:", round(cgpa, 2))

print("\nDeveloped by Umm e Aatika (FA23-BST-078)")
