import streamlit as st  # 👉 sabse pehle import

# Page Configuration
st.set_page_config(page_title="Unit Converter", layout="centered")

# Sidebar Info
st.sidebar.title("About Me")
st.sidebar.info("""
**I am Afshan**  
Python Developer in training 🐍  
Love building cool apps (and breaking a few 😅)  
Fuel: Chai ☕ & Curiosity 💡
""")

# App Title
st.title("🔁 Unit Converter")

# Conversion Type Selection
option = st.selectbox("Choose conversion type:", [
    "Kilometers to Miles",
    "Miles to Kilometers",
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius"
])

# Value Input
value = st.number_input("Enter value:", format="%.2f")

# Convert Button Logic
if st.button("Convert"):
    if option == "Kilometers to Miles":
        result = value * 0.621371
        st.success(f"{value} kilometers = {result:.2f} miles")
    elif option == "Miles to Kilometers":
        result = value / 0.621371
        st.success(f"{value} miles = {result:.2f} kilometers")
    elif option == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
        st.success(f"{value}°C = {result:.2f}°F")
    elif option == "Fahrenheit to Celsius":
        result = (value - 32) * 5/9
        st.success(f"{value}°F = {result:.2f}°C")


