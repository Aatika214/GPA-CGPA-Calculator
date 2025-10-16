# 🎓 GPA & CGPA Calculator App
# Author: Umm e Aatika (FA23-BST-078)
# Institution: COMSATS University Islamabad, Lahore Campus

import streamlit as st
import numpy as np
import pandas as pd

# App Title
st.title("🎓 GPA & CGPA Calculator App")
st.markdown("##### Developed by **Umm e Aatika (FA23-BST-078)** | COMSATS University Lahore Campus")

st.write("---")

# -------------------------------
# GPA Calculation Section
# -------------------------------
st.header("📘 GPA Calculation")

num_courses = st.number_input("Enter number of subjects this semester:", min_value=1, max_value=12, step=1)

grades = []
credits = []

for i in range(num_courses):
    col1, col2 = st.columns(2)
    with col1:
        g = st.number_input(f"Grade Points for Subject {i+1}", min_value=0.0, max_value=4.0, step=0.1)
    with col2:
        c = st.number_input(f"Credit Hours for Subject {i+1}", min_value=1.0, max_value=4.0, step=0.5)
    grades.append(g)
    credits.append(c)

if st.button("Calculate GPA"):
    grades = np.array(grades)
    credits = np.array(credits)
    gpa = np.sum(grades * credits) / np.sum(credits)
    st.success(f"🎯 Your GPA for this semester is **{gpa:.2f}**")

st.write("---")

# -------------------------------
# CGPA Calculation Section
# -------------------------------
st.header("📗 CGPA Calculation")

num_semesters = st.number_input("Enter total number of semesters completed:", min_value=1, max_value=12, step=1)

gpa_list = []
for i in range(num_semesters):
    g = st.number_input(f"GPA for Semester {i+1}", min_value=0.0, max_value=4.0, step=0.1)
    gpa_list.append(g)

if st.button("Calculate CGPA"):
    df = pd.DataFrame({
        "Semester": [f"Semester {i+1}" for i in range(num_semesters)],
        "GPA": gpa_list
    })
    cgpa = np.mean(gpa_list)
    st.dataframe(df)
    st.success(f"🏅 Your Overall CGPA is **{cgpa:.2f}**")

st.write("---")
st.caption("Developed by Umm e Aatika (FA23-BST-078)")
