# 🎓 Smart GPA & CGPA Calculator App
# Author: Umm e Aatika (FA23-BST-078)
# Institution: COMSATS University Islamabad, Lahore Campus

import streamlit as st
import numpy as np
import pandas as pd

# -------------------------------
# Function to convert marks into grade points
# -------------------------------
def marks_to_grade_point(marks):
    if marks >= 85:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 61:
        return 2.3
    elif marks >= 58:
        return 2.0
    elif marks >= 55:
        return 1.7
    elif marks >= 50:
        return 1.0
    else:
        return 0.0

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🎓 Smart GPA & CGPA Calculator App")
st.markdown("##### Developed by **Umm e Aatika (FA23-BST-078)** | COMSATS University Lahore Campus")
st.write("---")

# -------------------------------
# GPA Calculation Section
# -------------------------------
st.header("📘 Semester GPA Calculation")

num_courses = st.number_input("Enter number of subjects this semester:", min_value=1, max_value=12, step=1)

marks = []
credits = []
grade_points = []

for i in range(num_courses):
    col1, col2 = st.columns(2)
    with col1:
        m = st.number_input(f"Marks for Subject {i+1} (0–100):", min_value=0, max_value=100, step=1)
    with col2:
        c = st.number_input(f"Credit Hours for Subject {i+1}:", min_value=1.0, max_value=4.0, step=0.5)
    marks.append(m)
    credits.append(c)
    grade_points.append(marks_to_grade_point(m))

if st.button("Calculate GPA"):
    grades = np.array(grade_points)
    credits = np.array(credits)
    gpa = np.sum(grades * credits) / np.sum(credits)

    df = pd.DataFrame({
        "Subject": [f"Subject {i+1}" for i in range(num_courses)],
        "Marks": marks,
        "Grade Points": grade_points,
        "Credit Hours": credits
    })

    st.subheader("📄 Semester Summary")
    st.dataframe(df)
    st.success(f"🎯 Your GPA for this semester is **{gpa:.2f}**")

st.write("---")

# -------------------------------
# CGPA Calculation Section
# -------------------------------
st.header("📗 CGPA Calculation")

num_semesters = st.number_input("Enter number of semesters completed:", min_value=1, max_value=12, step=1)

gpa_list = []
for i in range(num_semesters):
    g = st.number_input(f"GPA for Semester {i+1}:", min_value=0.0, max_value=4.0, step=0.01)
    gpa_list.append(g)

if st.button("Calculate CGPA"):
    df_cgpa = pd.DataFrame({
        "Semester": [f"Semester {i+1}" for i in range(num_semesters)],
        "GPA": gpa_list
    })
    cgpa = np.mean(gpa_list)
    st.subheader("📘 CGPA Summary")
    st.dataframe(df_cgpa)
    st.success(f"🏅 Your Overall CGPA is **{cgpa:.2f}**")

st.write("---")
st.caption("Developed by Umm e Aatika (FA23-BST-078)")
