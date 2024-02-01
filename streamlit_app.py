import pandas as pd
import numpy as np
import streamlit as st
import plotly as px

st.title('Projekt zaliczeniowy z programowania dla analityki danych.')

data = st.file_uploader('Tu wrzuc swoje dane', type=['csv'])
if data is not None:
    df = pd.read_csv(data, na_values=[" ", np.nan])
    st.dataframe(df.head(15))

st.markdown("## Czyszczenie danych")

page = st.sidebar.selectbox('Wybierz stronę:', [''])



st.code("messy_data['Dimension_x'] = messy_data['Dimension_x'].replace(np.nan, np.random.normal(5.88, 0.77)).round(2)")

'''data2 = st.file_uploader('Tu wrzuc swoje dane', type=['csv'])
if data2 is not None:
    df_2 = pd.read_csv(data2, na_values=[" ", np.nan])
    st.dataframe(df_2.head(15))'''
    

px.express.box(data['Price'], title="Boxplot of prices of diamonds with outliers", height=500)




