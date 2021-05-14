from numpy.core.defchararray import index
import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
import matplotlib.pyplot as plt

def app():
    df_analysis = pd.read_csv('data/2015.csv')
    df_visual = pd.read_csv('data/2015.csv')
    cols = pd.read_csv('data/metadata/column_type_desc.csv')
    Categorical,Numerical,Object = utils.getColumnTypes(cols)
    cat_groups = {}
    unique_Category_val={}

    for i in range(len(Categorical)):
            unique_Category_val = {Categorical[i]: utils.mapunique(df_analysis, Categorical[i])}
            cat_groups = {Categorical[i]: df_visual.groupby(Categorical[i])}
            
    
    category = st.selectbox("Select Category ",Categorical)
    
    labels = unique_Category_val[category]
    sizes = (df_visual[category].value_counts()/df_visual[category].count())
    maxIndex = np.argmax(sizes)
    explode = []
    for i in range(len(labels)):
        if maxIndex==i:
            explode.append(0.1)
            
        else:
            explode.append(0)
    explode = tuple(explode)
    
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes,explode = explode, labels=labels, autopct='%1.1f%%',shadow=False, startangle=0)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)
    
    
    categoryObject=st.selectbox("Select " + (str)(category),unique_Category_val[category])
    colName = st.selectbox("Select Column ",Numerical)
    st.line_chart(cat_groups[category].get_group(categoryObject)[colName])
    
    #Showing details for the selected choices
    #st.write(cat_groups[category].get_group(categoryObject))
    
    #Basic analysis for the selected region
    st.write(cat_groups[category].get_group(categoryObject).describe())
 

    
    
    
   