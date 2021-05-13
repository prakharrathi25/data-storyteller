import os
import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import data_upload, data, model, machine_learning, metadata # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Data Storyteller Application")

# Add all your application here
app.add_page("Upload Data", data_upload.app)
app.add_page("Change Metadata", metadata.app)
app.add_page("Machine Learning", machine_learning.app)

# The main app
app.run()
