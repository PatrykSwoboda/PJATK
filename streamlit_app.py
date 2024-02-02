import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time

st.title('Projekt zaliczeniowy z programowania dla analityki danych.')
page = st.sidebar.selectbox('Wybierz stronę:', ['Przygotowanie danych i wizualizacja danych', 'Model regresji liniowej'])

if page == "Przygotowanie danych i wizualizacja danych":

    data = st.file_uploader('Importowanie pliku', type=['csv'])
    if data is not None:
        df = pd.read_csv(data, na_values=[" ", np.nan])
        my_bar = st.progress(0)
        for a in range(100):
            time.sleep(0.01)
            my_bar.progress(a+1)
        st.dataframe(df.head(15))
        
        st.markdown("## Czyszczenie danych")

        st.markdown("#### Ujednolicanie zbioru")
        
        st.markdown("#### Sposoby uzupełniania braków danych")
        st.code("messy_data['Dimension_x'] = messy_data['Dimension_x'].replace(np.nan, np.random.normal(5.88, 0.77)).round(2) \nmessy_data['Depth'] = messy_data['Depth'].replace(np.nan, messy_data['Depth'].mean()).round(2) \nmessy_data['Carat'] = messy_data['Carat'].apply(lambda x: my_list.pop(0) if pd.isna(x) else x)")
    
        st.markdown("## Wizualizacja rozrzutów i rozkładów zmiennych")

        status = st.radio("Wybierz typ wykresu", ('Wykres pudełkowy', 'Histogram', 'Wykres skrzypcowy'))
        if status == 'Wykres pudełkowy':
            
            col1, col2=st.columns(2)
            fig=px.box(df['Price'], title="Boxplot of prices of diamonds without outliers", height=500)
            col1.plotly_chart(fig)

            col1, col2=st.columns(2)
            fig=px.box(df[['Dimension_x', 'Dimension_y', 'Dimension_z', 'Carat']], title="Boxplots of dimensions and carat", height=500)
            col1.plotly_chart(fig)

            col1, col2=st.columns(2)
            fig=px.box(df[['Depth', 'Table']], title='Boxplots of depth and table of diamonds', height=500)
            col1.plotly_chart(fig)

        elif status == 'Histogram':
    
            col1, col2=st.columns(2)
            fig = make_subplots(rows=2, cols=4, subplot_titles=['Carat', 'Depth', 'Table', 'Price', 
                                'Dimension x', 'Dimension y', 'Dimension z'])
        
            trace0 = go.Histogram(x=df['Carat'], nbinsx=8)
            trace1 = go.Histogram(x=df['Depth'], nbinsx=8)
            trace2 = go.Histogram(x=df['Table'], nbinsx=8)
            trace3 = go.Histogram(x=df['Price'], nbinsx=8)
            trace4 = go.Histogram(x=df['Dimension_x'], nbinsx=8)
            trace5 = go.Histogram(x=df['Dimension_y'], nbinsx=8)
            trace6 = go.Histogram(x=df['Dimension_z'], nbinsx=8)
        
            fig.append_trace(trace0, 1, 1)
            fig.append_trace(trace1, 1, 2)
            fig.append_trace(trace2, 1, 3)
            fig.append_trace(trace3, 1, 4)
            fig.append_trace(trace4, 2, 1)
            fig.append_trace(trace5, 2, 2)
            fig.append_trace(trace6, 2, 3)
        
            col1.plotly_chart(fig)

        else:
    
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
    
        st.markdown("## Macierz korelacji")
    
        cor = df[['Carat','Dimension_x','Dimension_y','Dimension_z','Depth','Table','Price']].corr()
        col1, col2=st.columns(2)
        fig=px.imshow(cor, title='Heatmap as a correlation matrix of data', color_continuous_scale='amp', height=600)
        col1.plotly_chart(fig)
