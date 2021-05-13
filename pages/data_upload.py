import collections
from numpy.core.defchararray import lower
import streamlit as st
import numpy as np
import pandas as pd

# @st.cache
def app():
    st.markdown("## Data Upload")

    # Upload the dataset and save as csv
    st.markdown("### Upload a csv file for analysis.") 
    st.write("\n")
    
    # uploaded_files = st.file_uploader("Upload your CSV file here.", type='csv', accept_multiple_files=False)
    # # Check if file exists 
    # if uploaded_files:
    #     for file in uploaded_files:
    #         file.seek(0)
    #     uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
    #     raw_data = pd.concat(uploaded_data_read)
    
    # uploaded_files = st.file_uploader("Upload CSV", type="csv", accept_multiple_files=False)
    # print(uploaded_files, type(uploaded_files))
    # if uploaded_files:
    #     for file in uploaded_files:
    #         file.seek(0)
    #     uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
    #     raw_data = pd.concat(uploaded_data_read)
    
    # read temp data 
    data = pd.read_csv('data/2015.csv')


    ''' Load the data and save the columns with categories as a dataframe. 
    This section also allows changes in the numerical and categorical columns. '''
    if st.button("Load Data"):
        
        # Raw data 
        st.dataframe(data)

        # Generate a pandas profiling report
        # if st.button("Generate an analysis report"):
        # 	pass

        # Collect the categorical and numerical columns 
        
        numeric_cols = data.select_dtypes(include=np.number).columns.tolist()
        categorical_cols = list(set(list(data.columns)) - set(numeric_cols))
        
        # Save the columns as a dataframe or dictionary
        columns = []

        # Iterate through the numerical and categorical columns and save in columns 
        for col in numeric_cols:
            columns.append([col.lower(), 'numeric'])
        for col in categorical_cols:
            columns.append([col.lower(), 'categorical']) 
        
        # Save the columns as a dataframe with categories
        # Here column_name is the name of the field and the type is whether it's numerical or categorical
        columns_df = pd.DataFrame(data = columns, columns = ['column_name', 'type'])
        st.dataframe(columns_df)
        columns_df.to_csv('data/metadata/column_type_desc.csv')

        ''' Change the information about column types
        Here the info of the column types can be changed using dropdowns.
        The page is divided into two columns using beta columns 
        '''
        st.markdown("#### Change the information about column types")
        
        # Use two column technique 
        col1, col2 = st.beta_columns(2)

        # Design column 1 
        name = col1.selectbox("Select Column", data.columns)
        
        # Design column two 
        type = col2.selectbox("Select Column Type", ['numeric', 'categorical'])
        
        if st.button("Change the type"):
            # Set the value in the metadata and resave the file 
            col_metadata = pd.read_csv('data/metadata/column_type_desc.csv')
            col_metadata.loc[col_metadata['column_name'] == name, 'type'] = type
            col_metadata.to_csv('data/metadata/column_type_desc.csv', index = False)