from numpy.core.defchararray import index
import streamlit as st
import numpy as np
import pandas as pd
from pages import utils

def app():
    df_analysis = pd.read_csv('data/2015.csv')
    df_visual = pd.read_csv('data/2015.csv')
    cols = pd.read_csv('data/metadata/column_type_desc.csv')
    
    for i in range(len(cols)):
        if cols["type"][i]=='Categorical':
            cat = utils.mapunique(df_analysis, cols["column_name"][i])
            dg = df_visual.groupby("Region")
            for j in range(len(cat)):
                st.write(dg.get_group(cat[j]).head())
    
    st.write(df_analysis)
        # st.write(col[i]," ", utils.isCategorical(df[col[i]]))
    
    

    

    #gen_Metdata = pd.DataFrame(ColumnType)
    
    #if len(unis)<0.2*len(col):
    #    return False
    