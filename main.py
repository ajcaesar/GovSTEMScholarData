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
