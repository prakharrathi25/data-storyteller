import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
import os

def app():
	
	if 'main_data.csv' not in os.listdir('data'):
		st.markdown("Please upload data through `Upload Data` page!")
	else:
		df = pd.read_csv('data/main_data.csv')
		st.markdown("### A small demo to show redundant columns of a csv")

		redCols = utils.getRedundentColumns
		corr = df.corr(method='pearson')
		y_var = st.radio("Select the variable to be predicted (y)", options=corr.columns)
		th = st.slider("Threshold", min_value=0.05, max_value=0.95, value=0.25, step=0.01, format='%f')#, key=None, help=None)
		# st.write(df.col)
		redundantCols = utils.getRedundentColumns(corr, y_var, th)
		newDF = utils.newDF(df, redundantCols)
		# st.write("Redundant Columns:", redundantCols)
		st.write("Number of Columns Dropped: ",len(redundantCols))
		st.write("New Data: \n", newDF.head())

	