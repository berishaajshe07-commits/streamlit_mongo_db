
import streamlit as st
from pymongo import MongoClient

st.title("Sample MongoDB")

uri = st.secrets["MONGO_URI_ST"]

server = MongoClient(uri)
server.admin.command("ping")

db = server["name_tacker"]
collection = db["usernames"]
  
st.success("DB connection done!")

name = st.text_input("User name", "Filani")

if name:
    st.write(f"The current user name is **{name}**")
    collection.insert_one({"user_name": name})

