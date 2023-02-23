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
i = 0; 
while i < 10:
  #add in pH data 
  df1.at[i, "pH"] = float(df.iloc[0, 4*i + 3])
  df2.at[i, "pH"] = float(df.iloc[1, 4*i + 3])
  df3.at[i, "pH"] = float(df.iloc[2, 4*i + 3])
  df4.at[i, "pH"] = float(df.iloc[3, 4*i + 3])
  df5.at[i, "pH"] = float(df.iloc[4, 4*i + 3])
  df6.at[i, "pH"] = float(df.iloc[5, 4*i + 3])
  df7.at[i, "pH"] = float(df.iloc[6, 4*i + 3])
  df8.at[i, "pH"] = float(df.iloc[7, 4*i + 3])
  df9.at[i, "pH"] = float(df.iloc[8, 4*i + 3])
  df10.at[i, "pH"] = float(df.iloc[9, 4*i + 3])
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
  a = df.iloc[0, 4*i + 4]
  b = df.iloc[1, 4*i + 4]
  c = df.iloc[2, 4*i + 4]
  d = df.iloc[3, 4*i + 4]
  e = df.iloc[4, 4*i + 4]
  f = df.iloc[5, 4*i + 4]
  g = df.iloc[6, 4*i + 4]
  h = df.iloc[7, 4*i + 4]
  ij = df.iloc[8, 4*i + 4]
  k = df.iloc[9, 4*i + 4]
  if (i%2 == 1):
    df1.at[i, "Nitrite"] = float(a.split('/')[0])
    df2.at[i, "Nitrite"] = float(b.split('/')[0])
    df3.at[i, "Nitrite"] = float(c.split('/')[0])
    df4.at[i, "Nitrite"] = float(d.split('/')[0])
    df5.at[i, "Nitrite"] = float(e.split('/')[0])
    df6.at[i, "Nitrite"] = float(f.split('/')[0])
    df7.at[i, "Nitrite"] = float(g.split('/')[0])
    df8.at[i, "Nitrite"] = float(h.split('/')[0])
    df9.at[i, "Nitrite"] = float(ij.split('/')[0])
    df1.at[i, "Nitrate"] = float(a.split('/')[1])
    df2.at[i, "Nitrate"] = float(b.split('/')[1])
    df3.at[i, "Nitrate"] = float(c.split('/')[1])
    df4.at[i, "Nitrate"] = float(d.split('/')[1])
    df5.at[i, "Nitrate"] = float(e.split('/')[1])
    df6.at[i, "Nitrate"] = float(f.split('/')[1])
    df7.at[i, "Nitrate"] = float(g.split('/')[1])
    df8.at[i, "Nitrate"] = float(h.split('/')[1])
    df9.at[i, "Nitrate"] = float(ij.split('/')[1])
    if (i != 7):
      df10.at[i, "Nitrite"] = float(k.split('/')[0])
      df10.at[i, "Nitrate"] = float(k.split('/')[1])
    
      
  #add in Week data 
  df9.at[i, "Week"] = int(i + 1)
  df1.at[i, "Week"] = int(i + 1)
  df2.at[i, "Week"] = int(i + 1)
  df3.at[i, "Week"] = int(i + 1)
  df4.at[i, "Week"] = int(i + 1)
  df5.at[i, "Week"] = int(i + 1)
  df6.at[i, "Week"] = int(i + 1)
  df7.at[i, "Week"] = int(i + 1)
  df8.at[i, "Week"] = int(i + 1)
  df9.at[i, "Week"] = int(i + 1)
  df10.at[i, "Week"] = int(i + 1)
  i += 1

option = st.selectbox(
     'Pick your container',
     ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))

if option == '1':
  st.write(df1)
  st.line_chart(df1['Nitrite'])
  st.line_chart(df1['Nitrate'])
  st.line_chart(df1['pH'])
elif option == '2':
  st.write(df2)
  st.line_chart(df2['Nitrite'])
  st.line_chart(df2['Nitrate'])
  st.line_chart(df2['pH'])
elif option == '3':
  st.write(df3)
  st.line_chart(df3['Nitrite'])
  st.line_chart(df3['Nitrate'])
  st.line_chart(df3['pH'])
elif option == '4':
  st.write(df4)
  st.line_chart(df4['Nitrite'])
  st.line_chart(df4['Nitrate'])
  st.line_chart(df4['pH'])
elif option == '5':
  st.write(df5)
  st.line_chart(df5['Nitrite'])
  st.line_chart(df5['Nitrate'])
  st.line_chart(df5['pH'])
elif option == '6':
  st.write(df6)
  st.line_chart(df6['Nitrite'])
  st.line_chart(df6['Nitrate'])
  st.line_chart(df6['pH'])
elif option == '7':
  st.write(df7)
  st.line_chart(df7['Nitrite'])
  st.line_chart(df7['Nitrate'])
  st.line_chart(df7['pH'])
elif option == '8':
  st.write(df8)
  st.line_chart(df8['Nitrite'])
  st.line_chart(df8['Nitrate'])
  st.line_chart(df8['pH'])
elif option == '9':
  st.write(df9)
  st.line_chart(df9['Nitrite'])
  st.line_chart(df9['Nitrate'])
  st.line_chart(df9['pH'])
elif option == '10':
  st.write(df10)
  st.line_chart(df10['Nitrite'])
  st.line_chart(df10['Nitrate'])
  st.line_chart(df10['pH'])

