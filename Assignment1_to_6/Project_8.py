# Project 8: Create a Python Streamlit BMI Calculator Web App in Just 6 Minutes

import streamlit as st

def bmi_calculator():
    st.title("BMI Calculator")
    
    # Taking input for weight and height
    weight = st.number_input("Enter your weight (kg):", min_value=1)
    height = st.number_input("Enter your height (m):", min_value=0.1)

    # Checking if inputs are valid
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)  # Calculating BMI
        st.write(f"Your BMI is: {bmi:.2f}")

        # Providing feedback based on the BMI value
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")
    else:
        st.write("Please enter valid weight and height.")

bmi_calculator()
