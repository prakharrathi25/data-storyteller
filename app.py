import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from multipage import MultiPage
from pages import data_upload, machine_learning, metadata, data_visualize, redundant # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
display = Image.open('Logo.png')
display = np.array(display)
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
col1, col2 = st.beta_columns(2)
col1.image(display, width = 400)
col2.title("Data Storyteller Application")

# Dropdown menu for page selection
selected_page = st.selectbox("Select Page", ["Upload Data", "Change Metadata", "Machine Learning", "Data Analysis", "Y-Parameter Optimization"])

# Add all your application pages
if selected_page == "Upload Data":
    app.add_page("Upload Data", data_upload.app)
elif selected_page == "Change Metadata":
    app.add_page("Change Metadata", metadata.app)
elif selected_page == "Machine Learning":
    app.add_page("Machine Learning", machine_learning.app)
elif selected_page == "Data Analysis":
    app.add_page("Data Analysis", data_visualize.app)
elif selected_page == "Y-Parameter Optimization":
    app.add_page("Y-Parameter Optimization", redundant.app)

# The main app
app.run()
