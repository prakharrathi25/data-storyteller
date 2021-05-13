import os
import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import data_upload, data, model # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Data Storyteller Application")

# Add all your application here
app.add_page("Upload Data", data_upload.app)
app.add_page("Data", data.app)
app.add_page("Model", model.app)

# The main app
app.run()
