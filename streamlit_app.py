import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.title('Projekt zaliczeniowy z programowania dla analityki danych.')
page = st.sidebar.selectbox('Wybierz stronę:', [''])

data = st.file_uploader('Tu wrzuc swoje dane', type=['csv'])
if data is not None:
    df = pd.read_csv(data, na_values=[" ", np.nan])
    st.dataframe(df.head(15))
    
    st.markdown("## Czyszczenie danych")
    
    st.code("messy_data['Dimension_x'] = messy_data['Dimension_x'].replace(np.nan, np.random.normal(5.88, 0.77)).round(2)")

    st.markdown("## Wizualizacja rozrzutów i rozkładów zmiennych")
    
    col1, col2=st.columns(2)
    fig=px.box(df['Price'], title="Boxplot of prices of diamonds without outliers", height=500)
    col1.plotly_chart(fig)

    col1, col2=st.columns(2)
    fig=px.box(df[['Dimension_x', 'Dimension_y', 'Dimension_z', 'Carat']], title="Boxplots of dimensions and carat", height=500)
    col1.plotly_chart(fig)

    col1, col2=st.columns(2)
    fig=px.box(df[['Depth', 'Table']], title='Boxplots of depth and table of diamonds', height=500)
    col1.plotly_chart(fig)

    categorics = df[['Cut', 'Color', 'Clarity', 'Price']]
    
    col1, col2=st.columns(2)
    fig = px.violin(categorics, x='Cut', y='Price', points='all', box=True, 
               title='Violin chart of diamond cuts dependent on price')
    col1.plotly_chart(fig)

    col1, col2=st.columns(2)
    fig = px.violin(categorics, x='Color', y='Price', orientation='v', 
                title='Violin chart of diamond colors dependent on price')
    fig.update_layout(autosize=False, width=800, height=400)
    col1.plotly_chart(fig)

    col1, col2=st.columns(2)
    fig = px.violin(categorics, x='Clarity', y='Price', points='all', 
               title='Violin chart of diamond clarity dependent on price')
    col1.plotly_chart(fig)



