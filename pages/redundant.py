import streamlit as st
import numpy as np
import pandas as pd
from pages import utils

def app():
	df = pd.read_csv('data/2015.csv')## For now it is static!
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

	