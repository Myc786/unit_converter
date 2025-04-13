import streamlit as st

st.title("Unit Converter")

st.markdown("### Convert length, weight, and time instantly!")

st.write("Welcome! Select a category, enter a value, and get the converted result in real time!")

# Step 1: Select category
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Step 2: Select unit based on category
if category == "Length":
    unit = st.selectbox("Select a conversion", ["kilometers to miles", "miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select a conversion", ["kilograms to pounds"])
elif category == "Time":
    unit = st.selectbox("Select a conversion", ["seconds to minutes", "minutes to seconds", "minutes to hours", "hours to minutes", "days to hours"])

# Step 3: Input value
value = st.number_input("Enter the value to convert")

# Step 4: Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "kilometers to miles":
            return value * 0.621371
        elif unit == "miles to kilometers":
            return value / 0.621371
    elif category == "Weight":
        if unit == "kilograms to pounds":
            return value * 2.20462
    elif category == "Time":
        if unit == "seconds to minutes":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60 
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "hours to minutes":
            return value * 60
        elif unit == "days to hours":
            return value * 24
    return None  # Return None if no conversion is applicable

# Step 5: Trigger conversion
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Conversion could not be performed.")