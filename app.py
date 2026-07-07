import streamlit as st
from pymongo import MongoClient


# Title
st.title("BMI Calculator")


# MongoDB connection
uri = st.secrets["MONGO_URI_ST"]

server = MongoClient(uri)
server.admin.command("ping")

db = server["sample_mfix"]
collection = db["bmi_users"]

st.success("DB connection done!")


# Inputs
name = st.text_input("Name")

height = st.number_input(
    "Height (meters)",
    min_value=0.1
)

weight = st.number_input(
    "Weight (kg)",
    min_value=1.0
)


# Button
if st.button("Calculate BMI"):

    # BMI calculation
    bmi = weight / (height ** 2)


    # Outputs in Streamlit
    st.subheader("Results")

    st.write("Name:", name)
    st.write("Height:", height)
    st.write("Weight:", weight)
    st.write("BMI:", round(bmi, 2))


    # Register in MongoDB
    data = {
        "name": name,
        "height": height,
        "weight": weight,
        "bmi": round(bmi, 2)
    }

    collection.insert_one(data)

    st.success("Data saved in MongoDB!")