import numpy as np
import pandas as pd
import streamlit as st
from io import StringIO

df = pd.read_csv("Data Spreadsheet - Sheet1.csv")
df1 = pd.DataFrame(columns = ["Week", "pH", "Nitrate", "Nitrite"])
df2 = pd.DataFrame(columns = ["Week", "pH", "Nitrate", "Nitrite"])
df3 = pd.DataFrame(columns = ["Week", "pH", "Nitrate", "Nitrite"])
df4 = pd.DataFrame(columns = ["Week", "pH", "Nitrate", "Nitrite"])
df5 = pd.DataFrame(columns = ["Week", "pH", "Nitrate", "Nitrite"])
df6 = pd.DataFrame(columns = ["Week", "pH", "Nitrate", "Nitrite"])
df7 = pd.DataFrame(columns = ["Week", "pH", "Nitrate", "Nitrite"])
df8 = pd.DataFrame(columns = ["Week", "pH", "Nitrate", "Nitrite"])
df9 = pd.DataFrame(columns = ["Week", "pH", "Nitrate", "Nitrite"])
df10 = pd.DataFrame(columns = ["Week", "pH", "Nitrate", "Nitrite"])
st.write(df)

i = 0; 
for i < 10:
  df1.at[i]["pH"] = df.iloc[1, 4*i + 3]
  df2.at[i]["pH"] = df.iloc[2, 4*i + 3]
  df3.at[i]["pH"] = df.iloc[3, 4*i + 3]
  df4.at[i]["pH"] = df.iloc[4, 4*i + 3]
  df5.at[i]["pH"] = df.iloc[5, 4*i + 3]
  df6.at[i]["pH"] = df.iloc[6, 4*i + 3]
  df7.at[i]["pH"] = df.iloc[7, 4*i + 3]
  df8.at[i]["pH"] = df.iloc[8, 4*i + 3]
  df9.at[i]["pH"] = df.iloc[9, 4*i + 3]
  df10.at[i]["pH"] = df.iloc[10, 4*i + 3]
  i += 1
  
st.write(df1)
