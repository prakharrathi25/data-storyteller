# Import necessary libraries
import json
import pandas as pd 
import streamlit as st
# import sklearn 


def app():
    """This application helps in running machine learning models without having to write explicit code 
    by the user. It runs some basic models and let's the user select the X and y variables. 
    """
    
    # Load the data 
    data = pd.read_csv('data/main_data.csv')

    # Create the model parameters dictionary 
    params = {}

    # Use two column technique 
    col1, col2 = st.beta_columns(2)

    # Design column 1 
    y_var = col1.radio("Select the variable to be predicted (y)", options=data.columns)

    # Design column 2 
    X_var = col2.multiselect("Select the variables to be used for prediction (X)", options=data.columns)

    # Check if y not in X 
    if y_var in X_var:
        st.error("Warning! Y variable cannot be present in your X-variable. ")

    # Add to model parameters 
    params['prediction_vars'] = {
            'X': X_var,
            'y': y_var
    }

    # Option to select predition type 
    pred_type = st.radio("Select the type of process you want to run.", 
                        options=["Regression", "Classification"], 
                        help="Write about reg and classification")

    if st.button("Run Models"):
        st.write("Run Models. Need sklearn import")
        st.write(y_var)
        st.write(X_var)