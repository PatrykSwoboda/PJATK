import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import statsmodels.formula.api as smf
import time

st.title('Projekt zaliczeniowy z programowania dla analityki danych.')
page = st.sidebar.selectbox('Wybierz stronę:', ['Przygotowanie danych i wizualizacja danych', 'Model regresji liniowej'])
data = st.file_uploader('Importowanie pliku', type=['csv'])
if data is not None:
    df = pd.read_csv(data, na_values=[" ", np.nan])
    st.dataframe(df.head(15))

if page == "Przygotowanie danych i wizualizacja danych":
    st.markdown("## Czyszczenie danych")

    st.markdown("#### Ujednolicanie zbioru")
    st.code('messy_data["Clarity"] = messy_data["Clarity"].str.replace("i1", "I1").str.replace("si2", "SI2").str.replace("Si2", "SI2").str.replace("vvs1", "VVS1").str.replace("Vvs1", "VVS1").str.replace("if", "IF").str.replace("vvs2", "VVS2").str.replace("sI1", "SI1") \nmessy_data["Color"] = messy_data["Color"].str.replace("g", "G").str.replace("h", "H").str.replace("f", "F").str.replace("d", "D").str.replace("e", "E").str.replace("j", "J").str.replace("colorlEss", "ColorlEss").str.replace("ColorlEss", "Colorless") \nmessy_data["Cut"] = messy_data["Cut"].str.replace("premium", "Premium").str.replace("good", "Good").str.replace("fair", "Fair").str.replace("ideal", "Ideal").str.replace("very good", "Very Good").str.replace("Very good", "Very Good").str.replace("very Good", "Very Good")')
    st.code('messy_data.rename(columns={"carat": "Carat", " clarity": "Clarity", " color": "Color", " cut": "Cut", " x dimension": "Dimension_x", " y dimension": "Dimension_y", " z dimension": "Dimension_z", " depth": "Depth", " table": "Table", " price": "Price"}, inplace=True)')
    
    st.markdown("#### Sposoby uzupełniania braków danych użyte w projekcie")
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

    st.markdown("## Wykres punktowy w zależności od klarowności, ceny oraz rodzaju cięcia diamentu")

    cut_list = df['Cut'].unique()
    cut = st.selectbox("Wybierz rodzaj cięcia", cut_list) 

    col1, col2 = st.columns(2)

    fig = px.scatter(df[df['Cut'] == cut], x = 'Clarity', y = 'Price', 
                     title = 'Spot chart of clarity, price and type of diamond cut')
    col1.plotly_chart(fig,use_container_width = True)


else:
    st.markdown("## Parametry modelu regresji liniowej")
    df['Dimension_x^2'] = df['Dimension_x']**2

    model = smf.ols(formula='Price ~ I(Dimension_x**2) + C(Clarity)', data=df).fit()
    st.write(model.summary())

    st.markdown("## Wykres modelu regresji liniowej")

    my_bar = st.progress(0)
    for a in range(100):
        time.sleep(0.01)
        my_bar.progress(a+1)
    
    col1, col2=st.columns(2)
    fig = px.scatter(df, "Price", "Dimension_x^2", "Clarity", trendline="ols", trendline_scope="overall", 
           title="Regression line of diamond prices depended for squared length and clarity", height=600)
    col1.plotly_chart(fig)

    st.markdown("## Wykres reszt modelu")
    df['residuals'] = model.resid

    for a in range(100):
        time.sleep(0.01)
        my_bar.progress(a+1)
    
    col1, col2=st.columns(2)
    fig = px.scatter(df, "Price", "residuals", 
                     title="Model residuals plot of year vs squared length and clarity", height=600)
    fig.update_yaxes({'zerolinecolor':'red'})
    col1.plotly_chart(fig)
