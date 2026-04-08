import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")

st.title("🧮 Basic Calculator")

# =========================
# INPUTS
# =========================
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=0.0)

with col2:
    num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Select Operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
)

# =========================
# CALCULATION
# =========================
if st.button("Calculate"):

    if operation == "Addition (+)":
        result = num1 + num2

    elif operation == "Subtraction (-)":
        result = num1 - num2

    elif operation == "Multiplication (*)":
        result = num1 * num2

    elif operation == "Division (/)":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "❌ Cannot divide by zero"

    st.success(f"Result: {result}")