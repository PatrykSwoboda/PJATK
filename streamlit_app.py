import pandas as pd
import numpy as np
import streamlit as st

st.title('Projekt zaliczeniowy z programowania dla analityki danych.')

st.markdown("## Czyszczenie danych")

data = st.file_uploader('Tu wrzuc swoje dane', type=['csv'])
if data is not None:
    df = pd.read_csv(data, na_values=[" ", np.nan])
    st.dataframe(df.head(15))

st.code("messy_data['Dimension_x'] = messy_data['Dimension_x'].replace(np.nan, np.random.normal(5.88, 0.77)).round(2)")

data = st.file_uploader('Tu wrzuc swoje dane', type=['csv'])
if data is not None:
    df = pd.read_csv(data, na_values=[" ", np.nan])
    st.dataframe(df.head(15))
    
px.box(messy_data['Price'], title="Boxplot of prices of diamonds with outliers", height=500)




