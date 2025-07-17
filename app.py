'''Trabajando la interfaz WEB'''
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

df = pd.read_csv(
    r'D:\workspace_data_science\repositorios_clonados\vehicles_env\vehicles_us.csv')
# Agregando el dato -1 para tanques desconocidos
df['cylinders'] = df['cylinders'].fillna(-1)
# Filtrando los tanques desconocidos:
df2 = df[~(df['cylinders'] == -1)]

# El encabezado con streamlit
st.header('Graficas Intercativas "Vehiculos en USA"')

# Implementacion de una casilla que permita la creacion del Histograma
hist1 = st.checkbox('Construccion de Histograma')
scat1 = st.checkbox('Construccion de Grafico de Dispersion')

if hist1:
    # Construccion del histograma con plotly
    st.write('Histograma a continuacion:')
    Histogram1 = go.Figure(
        data=[go.Histogram(x=df2['cylinders'], marker_color='skyblue')])
    # Titulo:
    Histogram1.update_layout(
        title='Frecuencias en la capacidad de "Tanques"',
        title_x=0.5,
        xaxis_title='Capacidad del "Tanque"',
        yaxis_title='Cantidad de Unidades Vehiculares en "Miles"')
    st.plotly_chart(Histogram1)
