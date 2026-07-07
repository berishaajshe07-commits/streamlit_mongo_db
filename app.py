import streamlit as st
from pymongo import MongoClient


# Title
st.title("BMI Calculator")


# MongoDB connection
uri = st.secrets["MONGO_URI_ST"]

server = MongoClient(uri)
server.admin.command("ping")

db = server["BMI_database"]
collection = db["users"]

st.success("DB connection done!")


# Inputs
name = st.text_input("Name")

height = st.number_input(
    "Height (m)",
    min_value=0.1
)

weight = st.number_input(
    "Weight (kg)",
    min_value=1.0
)


# Calculate BMI and save data
if st.button("Calculate BMI"):

    bmi = weight / (height ** 2)


    # Outputs in Streamlit
    st.subheader("Results")

    st.write("Name:", name)
    st.write("Height:", height)
    st.write("Weight:", weight)
    st.write("BMI:", round(bmi, 2))


    # Register data in MongoDB
    user = {
        "name": name,
        "height": height,
        "weight": weight,
        "bmi": round(bmi, 2)
    }

    collection.insert_one(user)

    st.success("Data saved in MongoDB!")