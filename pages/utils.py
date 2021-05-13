import numpy as np 
import pandas as pd 
from pandas.api.types import is_numeric_dtype

def isCategorical(col):
    unis = np.unique(col)
    if len(unis)<0.2*len(col):
        return True
    return False

def isNumerical(col):
    return is_numeric_dtype(col)

def genMetaData(df):
    col = df.columns
    ColumnType = [] 
    for i in range(len(col)):
        if isCategorical(df[col[i]]):
            ColumnType.append((col[i],"Categorical"))
        
        elif is_numeric_dtype(df[col[i]]):
            ColumnType.append((col[i],"Numerical"))
        
        else:
            ColumnType.append((col[i],"Object"))
        
    return ColumnType


def makeMapDict(col): 
    uniqueVals = list(np.unique(col))
    uniqueVals.sort()
    dict_ = {uniqueVals[i]: i for i in range(len(uniqueVals))}
    return dict_

def mapunique(df, colName):
    dict_ = makeMapDict(df[colName])
    cat = np.unique(df[colName])
    df[colName] =  df[colName].map(dict_)
    return cat 


if __name__ == '__main__':
    df = {"Name": ["salil", "saxena", "for", "int"]}
    df = pd.DataFrame(df)
    print("Mapping dict: ", makeMapDict(df["Name"]))
    print("original df: ")
    print(df.head())
    pp = mapunique(df, "Name")
    print("New df: ")
    print(pp.head())
