import streamlit as st

st.title("Unit Converter App")
st.write("Convert between different units of measurement.")

conversion_type = st.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    options = {"Meters": 1, "Kilometers": 1000, "Feet": 0.3048, "Miles": 1609.34}
    from_unit = st.selectbox("From", options.keys())
    to_unit = st.selectbox("To", options.keys())
    value = st.number_input("Enter the value:")
    result = value * options[from_unit] / options[to_unit]
    st.write(f"Result: {result} {to_unit}")

elif conversion_type == "Weight":
    options = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495}
    from_unit = st.selectbox("From", options.keys())
    to_unit = st.selectbox("To", options.keys())
    value = st.number_input("Enter the value:")
    result = value * options[from_unit] / options[to_unit]
    st.write(f"Result: {result} {to_unit}")

elif conversion_type == "Temperature":
    temp = st.number_input("Enter temperature:")
    scale = st.radio("Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])

    if scale == "Celsius":
        result = (temp - 32) * 5/9 if st.radio("From:", ["Fahrenheit"]) else temp - 273.15
    elif scale == "Fahrenheit":
        result = (temp * 9/5) + 32 if st.radio("From:", ["Celsius"]) else (temp - 273.15) * 9/5 + 32
    elif scale == "Kelvin":
        result = temp + 273.15 if st.radio("From:", ["Celsius"]) else (temp - 32) * 5/9 + 273.15
    st.write(f"Result: {result} {scale}")
