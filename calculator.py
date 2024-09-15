import streamlit as st

st.title("Simple Calculator")


num1 = st.number_input("Enter the first number",value=0)
num2 = st.number_input("Enter the second number",value=0)

choice  = st.selectbox("SELECT A OPERATION",["+","-","*","/","//","%"])


if choice == "+":
    result = num1+num2
    if st.button("Calculate"):
        st.subheader(f"Addition of {num1} and {num2} is : {result}")
        st.balloons()
if choice == "-":
    result = num1-num2
    if st.button("Calculate"):
        st.subheader(f"Subtraction of {num1} and {num2} is : {result}")
        st.balloons()
if choice == "*":
    result = num1*num2
    if st.button("Calculate"):
        st.subheader(f"Multiplication of {num1} and {num2} is : {result}")
        st.balloons()
if choice == "/":
    result = num1/num2
    if st.button("Calculate"):
        st.subheader(f"Division of {num1} and {num2} is : {result}")
        st.balloons()

if choice == "%":
    result = num1%num2
    if st.button("Calculate"):
        st.subheader(f"Modulus of {num1} and {num2} is : {result}")
        st.balloons()

if choice == "//":
    result = num1//num2
    if st.button("Calculate"):
        st.subheader(f"Integer Division of {num1} and {num2} is : {result}")
        st.balloons()

