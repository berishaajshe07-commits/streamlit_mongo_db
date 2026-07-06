
import streamlit as st
from pymongo import MongoClient

st.title("Sample MongoDB :sunglasses:")


uri = st.secrets["MONGO_URI_ST"]

client = MongoClient(uri)
client.admin.command("ping")
  
st.success("DB connection done!")