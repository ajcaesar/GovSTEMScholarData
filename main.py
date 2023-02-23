import numpy as np
import pandas as pd
import streamlit as st
from io import StringIO

df = pd.read_csv("Data Spreadsheet - Sheet1.csv")
df1 = pd.DataFrame(columns = ["Week", "pH", "Nitrite", "Nitrate", "Water Added"])
df2 = pd.DataFrame(columns = ["Week", "pH", "Nitrite", "Nitrate", "Water Added"])
df3 = pd.DataFrame(columns = ["Week", "pH", "Nitrite", "Nitrate", "Water Added"])
df4 = pd.DataFrame(columns = ["Week", "pH", "Nitrite", "Nitrate", "Water Added"])
df5 = pd.DataFrame(columns = ["Week", "pH", "Nitrite", "Nitrate", "Water Added"])
df6 = pd.DataFrame(columns = ["Week", "pH", "Nitrite", "Nitrate", "Water Added"])
df7 = pd.DataFrame(columns = ["Week", "pH", "Nitrite", "Nitrate", "Water Added"])
df8 = pd.DataFrame(columns = ["Week", "pH", "Nitrite", "Nitrate", "Water Added"])
df9 = pd.DataFrame(columns = ["Week", "pH", "Nitrite", "Nitrate", "Water Added"])
df10 = pd.DataFrame(columns = ["Week", "pH", "Nitrite", "Nitrate", "Water Added"])
st.write(df)
st.write(type(df.iloc[0, 4]))
i = 0; 
while i < 10:
  #add in pH data 
  df1.at[i, "pH"] = df.iloc[0, 4*i + 3]
  df2.at[i, "pH"] = df.iloc[1, 4*i + 3]
  df3.at[i, "pH"] = df.iloc[2, 4*i + 3]
  df4.at[i, "pH"] = df.iloc[3, 4*i + 3]
  df5.at[i, "pH"] = df.iloc[4, 4*i + 3]
  df6.at[i, "pH"] = df.iloc[5, 4*i + 3]
  df7.at[i, "pH"] = df.iloc[6, 4*i + 3]
  df8.at[i, "pH"] = df.iloc[7, 4*i + 3]
  df9.at[i, "pH"] = df.iloc[8, 4*i + 3]
  df10.at[i, "pH"] = df.iloc[9, 4*i + 3]
  #add in water added data 
  df1.at[i, "Water Added"] = df.iloc[0, 4*i + 5]
  df2.at[i, "Water Added"] = df.iloc[1, 4*i + 5]
  df3.at[i, "Water Added"] = df.iloc[2, 4*i + 5]
  df4.at[i, "Water Added"] = df.iloc[3, 4*i + 5]
  df5.at[i, "Water Added"] = df.iloc[4, 4*i + 5]
  df6.at[i, "Water Added"] = df.iloc[5, 4*i + 5]
  df7.at[i, "Water Added"] = df.iloc[6, 4*i + 5]
  df8.at[i, "Water Added"] = df.iloc[7, 4*i + 5]
  df9.at[i, "Water Added"] = df.iloc[8, 4*i + 5]
  df10.at[i, "Water Added"] = df.iloc[9, 4*i + 5]
  #add in nitrite data 
  df1.at[i, "Nitrite"] = (df.iloc[0, 4*i + 4])[0:(df.iloc[0, 4*i + 4].index('/'))]
  df2.at[i, "Nitrite"] = df.iloc[1, 4*i + 4][0:(df.iloc[1, 4*i + 4].index('/'))]
  df3.at[i, "Nitrite"] = df.iloc[2, 4*i + 4][0:(df.iloc[2, 4*i + 4].index('/'))]
  df4.at[i, "Nitrite"] = df.iloc[3, 4*i + 4][:df.iloc[3, 4*i + 4].index('/')]
  df5.at[i, "Nitrite"] = df.iloc[4, 4*i + 4][:df.iloc[4, 4*i + 4].index('/')]
  df6.at[i, "Nitrite"] = df.iloc[5, 4*i + 4][:df.iloc[5, 4*i + 4].index('/')]
  df7.at[i, "Nitrite"] = df.iloc[6, 4*i + 4][:df.iloc[6, 4*i + 4].index('/')]
  df8.at[i, "Nitrite"] = df.iloc[7, 4*i + 4][:df.iloc[7, 4*i + 4].index('/')]
  df9.at[i, "Nitrite"] = df.iloc[8, 4*i + 4][:df.iloc[8, 4*i + 4].index('/')]
  df10.at[i, "Nitrite"] = df.iloc[9, 4*i + 4][:df.iloc[9, 4*i + 4].index('/')]
  #add in Week data 
  df9.at[i, "Week"] = i + 1
  df1.at[i, "Week"] = i + 1
  df2.at[i, "Week"] = i + 1
  df3.at[i, "Week"] = i + 1
  df4.at[i, "Week"] = i + 1
  df5.at[i, "Week"] = i + 1
  df6.at[i, "Week"] = i + 1
  df7.at[i, "Week"] = i + 1
  df8.at[i, "Week"] = i + 1
  df9.at[i, "Week"] = i + 1
  df10.at[i, "Week"] = i + 1
  i += 1
  
st.write(df1)
st.write(df2)
st.write(df3)
st.write(df4)
st.write(df5)
st.write(df6)
st.write(df7)
st.write(df8)
st.write(df9)
st.write(df10)

