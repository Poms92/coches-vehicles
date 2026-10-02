import streamlit as st
import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv('vehicles_us.csv')
st.header('Panel de anuncios de venta de coches usados')
precio_modelo = st.button('Precio por modelo') 
if precio_modelo: 
    fig = go.Figure() 
    fig.add_trace(go.Histogram(x=df['price']))
    st.write('Dsitribución de precios por modelo')
    st.plotly_chart(fig) 
mostrar_dispersion = st.button('Ver dispersión de precio y año del modelo')
if mostrar_dispersion:
    fig = go.Figure() 
    fig.add_trace(go.Scatter(x=df['model_year'], y=df['price'], mode='markers'))
    st.write('Dispersión de precio y año del modelo')
    st.plotly_chart(fig)