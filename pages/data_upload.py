import streamlit as st
import numpy as np
import pandas as pd

def app():
    st.markdown("## Data Upload")

    # Upload the dataset and save as csv
    st.markdown("### Upload files for analysis. These finals should have the same") 
    st.write("\n")
    uploaded_files = st.file_uploader("Upload CSV files", type="csv", accept_multiple_files=True)
    if uploaded_files:
        for file in uploaded_files:
            file.seek(0)
        uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
        raw_data = pd.concat(uploaded_data_read)

    # Load the data 
    if st.button("Load Data"):
        
    	# Raw data 
    	st.dataframe(raw_data)

    	# Generate a pandas profiling report
    	if st.button("Generate an analysis report"):
    		pass

    	# Show the columns in the sidebar 
    	column = st.sidebar.selectbox("Select the column:", raw_data.columns)
