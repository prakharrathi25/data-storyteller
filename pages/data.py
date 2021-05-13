import streamlit as st
import numpy as np
import pandas as pd
from streamlit import uploaded_file_manager

def app():
    st.title('Data')

    st.write("This is the `Data` page of the multi-page app.")

    st.write("The following is the DataFrame of the `iris` dataset.")