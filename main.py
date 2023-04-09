import numpy as np
import pandas as pd
import streamlit as st
from io import StringIO

st.title('The Effect of Microplastic Presence on Organic Matter Decomposition')
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
    df1.at[i-1, "Nitrite"] = float(a.split('/')[0])
    df2.at[i-1, "Nitrite"] = float(b.split('/')[0])
    df3.at[i-1, "Nitrite"] = float(c.split('/')[0])
    df4.at[i-1, "Nitrite"] = float(d.split('/')[0])
    df5.at[i-1, "Nitrite"] = float(e.split('/')[0])
    df6.at[i-1, "Nitrite"] = float(f.split('/')[0])
    df7.at[i-1, "Nitrite"] = float(g.split('/')[0])
    df8.at[i-1, "Nitrite"] = float(h.split('/')[0])
    df9.at[i-1, "Nitrite"] = float(ij.split('/')[0])
    df1.at[i-1, "Nitrate"] = float(a.split('/')[1])
    df2.at[i-1, "Nitrate"] = float(b.split('/')[1])
    df3.at[i-1, "Nitrate"] = float(c.split('/')[1])
    df4.at[i-1, "Nitrate"] = float(d.split('/')[1])
    df5.at[i-1, "Nitrate"] = float(e.split('/')[1])
    df6.at[i-1, "Nitrate"] = float(f.split('/')[1])
    df7.at[i-1, "Nitrate"] = float(g.split('/')[1])
    df8.at[i-1, "Nitrate"] = float(h.split('/')[1])
    df9.at[i-1, "Nitrate"] = float(ij.split('/')[1])
    if (i != 7):
      df10.at[i, "Nitrite"] = float(k.split('/')[0])
      df10.at[i, "Nitrate"] = float(k.split('/')[1])
      df10.at[i-1, "Nitrite"] = float(k.split('/')[0])
      df10.at[i-1, "Nitrate"] = float(k.split('/')[1])
   
  #add in water data 
  df1.at[i, "Water Added"] = 0.0
  df2.at[i, "Water Added"] = 0.0
  df3.at[i, "Water Added"] = 0.0
  df4.at[i, "Water Added"] = 0.0
  df5.at[i, "Water Added"] = 0.0
  df6.at[i, "Water Added"] = 0.0
  df7.at[i, "Water Added"] = 0.0
  df8.at[i, "Water Added"] = 0.0
  df9.at[i, "Water Added"] = 0.0
  df10.at[i, "Water Added"] = 0.0
  
  l = df.iloc[0, 4*i + 5]
  m = df.iloc[1, 4*i + 5]
  n = df.iloc[2, 4*i + 5]
  o = df.iloc[3, 4*i + 5]
  p = df.iloc[4, 4*i + 5]
  q = df.iloc[5, 4*i + 5]
  r = df.iloc[6, 4*i + 5]
  s = df.iloc[7, 4*i + 5]
  t = df.iloc[8, 4*i + 5]
  u = df.iloc[9, 4*i + 5]
  
  if not pd.isnull(df.iloc[0, 4*i + 5]):
    if ("m" in l):
      df1.at[i, "Water Added"] = float(l.split('m')[0])
  if not pd.isnull(df.iloc[1, 4*i + 5]):
    if ("m" in m):
      df2.at[i, "Water Added"] = float(m.split('m')[0])
  if not pd.isnull(df.iloc[2, 4*i + 5]):
    if ("m" in n):
      df3.at[i, "Water Added"] = float(n.split('m')[0])
  if not pd.isnull(df.iloc[3, 4*i + 5]):
    if ("m" in o):
      df4.at[i, "Water Added"] = float(o.split('m')[0])
  if not pd.isnull(df.iloc[4, 4*i + 5]):
    if ("m" in p):
      df5.at[i, "Water Added"] = float(p.split('m')[0])
  if not pd.isnull(df.iloc[5, 4*i + 5]):
    if ("m" in q):
      df6.at[i, "Water Added"] = float(q.split('m')[0])
  if not pd.isnull(df.iloc[6, 4*i + 5]):
    if ("m" in r):
      df7.at[i, "Water Added"] = float(r.split('m')[0])
  if not pd.isnull(df.iloc[7, 4*i + 5]):
    if ("m" in s):
      df8.at[i, "Water Added"] = float(s.split('m')[0])
  if not pd.isnull(df.iloc[8, 4*i + 5]):
    if ("m" in t):
      df9.at[i, "Water Added"] = float(t.split('m')[0])
  if not pd.isnull(df.iloc[9, 4*i + 5]):
    if ("m" in u):
      df10.at[i, "Water Added"] = float(u.split('m')[0])
    
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
  
 #combine nitrate onto one graph 
dfNitrate = pd.DataFrame({
'Container number': [f"{d} Days" for d in [1, 2, 3, 4, 5]],
        'Can 1': df2["Nitrate"],
        'Can 2': df4["Nitrate"],
        'Can 3': df6["Nitrate"],
        'Can 4': df8["Nitrate"],
        'Can 5': df10["Nitrate"],
},
  columns=['Can 1 (Og)', 'Can 2 (3g)', 'Can 3 (6g)', 'Can 4 (12g)', 'Can 5 (18g)']
)

dfNitrite = pd.DataFrame({
'Container number': [f"{d} Days" for d in [1, 2, 3, 4, 5]],
        'Can 1': df2["Nitrite"],
        'Can 2': df4["Nitrite"],
        'Can 3': df6["Nitrite"],
        'Can 4': df8["Nitrite"],
        'Can 5': df10["Nitrite"],
},
  columns=['Can 1 (Og)', 'Can 2 (3g)', 'Can 3 (6g)', 'Can 4 (12g)', 'Can 5 (18g)']
)

dfpH = pd.DataFrame({
'Container number': [f"{d} Days" for d in [1, 2, 3, 4, 5]],
        'Can 1': df2["pH"],
        'Can 2': df4["pH"],
        'Can 3': df6["pH"],
        'Can 4': df8["pH"],
        'Can 5': df10["pH"],
},
  columns=['Can 1 (Og)', 'Can 2 (3g)', 'Can 3 (6g)', 'Can 4 (12g)', 'Can 5 (18g)']
)

option = st.selectbox(
     'Pick your container/statistic',
     ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'pH', 'Nitrite', 'Nitrate'))

if option == '1':
  st.write(df1)
  st.line_chart(df1['Nitrite'])
  st.line_chart(df1['Nitrate'])
  st.line_chart(df1['pH'])
  st.line_chart(df1['Water Added'])
elif option == '2':
  st.write(df2)
  st.line_chart(df2['Nitrite'])
  st.line_chart(df2['Nitrate'])
  st.line_chart(df2['pH'])
  st.line_chart(df2['Water Added'])
elif option == '3':
  st.write(df3)
  st.line_chart(df3['Nitrite'])
  st.line_chart(df3['Nitrate'])
  st.line_chart(df3['pH'])
  st.line_chart(df3['Water Added'])
elif option == '4':
  st.write(df4)
  st.line_chart(df4['Nitrite'])
  st.line_chart(df4['Nitrate'])
  st.line_chart(df4['pH'])
  st.line_chart(df4['Water Added'])
elif option == '5':
  st.write(df5)
  st.line_chart(df5['Nitrite'])
  st.line_chart(df5['Nitrate'])
  st.line_chart(df5['pH'])
  st.line_chart(df5['Water Added'])
elif option == '6':
  st.write(df6)
  st.line_chart(df6['Nitrite'])
  st.line_chart(df6['Nitrate'])
  st.line_chart(df6['pH'])
  st.line_chart(df6['Water Added'])
elif option == '7':
  st.write(df7)
  st.line_chart(df7['Nitrite'])
  st.line_chart(df7['Nitrate'])
  st.line_chart(df7['pH'])
  st.line_chart(df7['Water Added'])
elif option == '8':
  st.write(df8)
  st.line_chart(df8['Nitrite'])
  st.line_chart(df8['Nitrate'])
  st.line_chart(df8['pH'])
  st.line_chart(df8['Water Added'])
elif option == '9':
  st.write(df9)
  st.line_chart(df9['Nitrite'])
  st.line_chart(df9['Nitrate'])
  st.line_chart(df9['pH'])
  st.line_chart(df9['Water Added'])
elif option == '10':
  st.write(df10)
  st.line_chart(df10['Nitrite'])
  st.line_chart(df10['Nitrate'])
  st.line_chart(df10['pH'])
  st.line_chart(df10['Water Added'])
elif option == 'pH':
  st.line_chart(data = dfpH, x = "Can #", y = "pH")
  st.line_chart(df1['pH'])
  st.line_chart(df2['pH'])
  st.line_chart(df3['pH'])
  st.line_chart(df4['pH'])
  st.line_chart(df5['pH'])
  st.line_chart(df6['pH'])
  st.line_chart(df7['pH'])
  st.line_chart(df8['pH'])
  st.line_chart(df9['pH'])
  st.line_chart(df10['pH'])
elif option == 'Nitrite':
  st.line_chart(data = dfNitrite, x = "Can #", y = "Nitrite (in ppm)")
  st.line_chart(df1['Nitrite'])
  st.line_chart(df2['Nitrite'])
  st.line_chart(df3['Nitrite'])
  st.line_chart(df4['Nitrite'])
  st.line_chart(df5['Nitrite'])
  st.line_chart(df6['Nitrite'])
  st.line_chart(df7['Nitrite'])
  st.line_chart(df8['Nitrite'])
  st.line_chart(df9['Nitrite'])
  st.line_chart(df10['Nitrite'])
elif option == 'Nitrate':
  st.line_chart(data = dfNitrate, x = "Can #", y="Nitrate (in ppm)")
  st.line_chart(df1['Nitrate'])
  st.line_chart(df2['Nitrate'])
  st.line_chart(df3['Nitrate'])
  st.line_chart(df4['Nitrate'])
  st.line_chart(df5['Nitrate'])
  st.line_chart(df6['Nitrate'])
  st.line_chart(df7['Nitrate'])
  st.line_chart(df8['Nitrate'])
  st.line_chart(df9['Nitrate'])
  st.line_chart(df10['Nitrate'])
