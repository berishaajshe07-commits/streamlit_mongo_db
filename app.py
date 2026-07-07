import streamlit as st
from pymongo import MongoClient


# Title
st.title("BMI Calculator")


# MongoDB connection
uri = st.secrets["MONGO_URI_ST"]

client = MongoClient(uri)

# Check connection
client.admin.command("ping")

st.success("DB connection done!")


# Database and new collection
db = client["sample_mfix"]
collection = db["bmi_records"]


# Inputs
name = st.text_input("Name")

height = st.number_input(
    "Height (meters)",
    min_value=0.1,
    step=0.01
)

weight = st.number_input(
    "Weight (kg)",
    min_value=1.0,
    step=0.1
)


# Button
if st.button("Calculate BMI"):

    if name and height and weight:

        # BMI calculation
        bmi = weight / (height ** 2)

        # Show outputs in Streamlit
        st.subheader("Results")

        st.write("Name:", name)
        st.write("Height:", height)
        st.write("Weight:", weight)
        st.write("BMI:", round(bmi, 2))


        # Save in MongoDB
        record = {
            "name": name,
            "height": height,
            "weight": weight,
            "bmi": round(bmi, 2)
        }

        collection.insert_one(record)

        st.success("Data registered in MongoDB!")

    else:
        st.warning("Please fill all fields")