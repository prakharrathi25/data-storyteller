# Import necessary libraries
import json
import joblib
import os

import pandas as pd
import streamlit as st

# Machine Learning 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier

def app():

    # Read the data 
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
    else:
        data = pd.read_csv('data/main_data.csv')

    # Also read the column types 
    types = pd.read_csv('data/metadata/column_type_desc.csv')
    # Load the model parameters
    with open('data/metadata/model_params.json') as f:
        params = json.load(f)

    X_var = params['X']
    y_var = params['y']
    pred_type = params['pred_type']

    st.write(f"""You ran a machine learning model with the following parameters:\n
    Prediction Variables: {X_var}
    Predicted Variable: {y_var}
    
    In this section you can mainpulate the X_values to see how the y_variables will change! 
    """)

    for i in range(len(X_var)):
        col = X_var[i]
        st.write(col)

        # Check column type 
        type = types[types['column_name'] == col]['type'].values[0]
        if type == 'numerical':
            min_val = float(round(data[col].min(), 1))
            max_val = float(round(data[col].max(), 1))

            col_value = st.slider(label=col, min_value=min_val, max_value=max_val, step=(max_val-min_val)/10)
