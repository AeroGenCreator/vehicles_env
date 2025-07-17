'''Trabajando la interfaz WEB'''
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

df = pd.read_csv('vehicles_us.csv')
# Agregando el dato -1 para tanques desconocidos
df['cylinders'] = df['cylinders'].fillna(-1)
# Filtrando los tanques desconocidos:
df2 = df[~(df['cylinders'] == -1)]

# El encabezado con streamlit
st.header('Graficas Intercativas "Vehiculos en USA"')

# Explicacion breve de la interfaz
st.write('Marque una casilla:')
# Implementacion de una casilla que permita la creacion del Histograma
hist1 = st.checkbox('Construccion de Histograma')
scat1 = st.checkbox('Construccion de Grafico de Dispersion')
table1 = st.checkbox('Mostrar "Tabla de Datos Original"')

if hist1:
    # Construccion del histograma con plotly
    st.write('Histograma a continuacion:')
    Histogram1 = go.Figure(
        data=[go.Histogram(x=df2['cylinders'], nbinsx=24)])
    # Titulo:
    Histogram1.update_layout(
        title='Frecuencias en la capacidad de "Tanques"',
        xaxis_title='Capacidad del "Tanque"',
        yaxis_title='Cantidad de Unidades Vehiculares en "Miles"')
    st.plotly_chart(Histogram1, use_container_width=True)

if scat1:
    # Construccion del scatter graph con plotly
    st.write('Grafico de dispersion a continuacion:')
    scatter1 = go.Figure(data=[go.Scatter(
        x=df2['odometer'], y=df2['price'], mode='markers', marker_color='orange')])
    scatter1.update_layout(
        title_text='Relacion entre "Gasto Total" y "Capacidad de Tanques"')
    st.plotly_chart(scatter1, use_container_width=True)

if table1:
    # Tabla armada con pandas
    st.dataframe(df2)
