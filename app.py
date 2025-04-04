import pandas as pd
import plotly.express as px
import streamlit as st


df = pd.read_csv('vehicles_us.csv')


# Encabezado de la apalicacion
st.header('ANALISIS EXPLORATORIO DE DATOS DE VEHICULOS')
# Boton para contruir un histograma
if st.button('Construir histograma'):
    st.write("Histograma de la columna  'odometer'")
    if 'odometer' in df.columns:
        fig = px.histogram(df, x='odometer', title='histograma de odometro')
    else:
        fig = px.histogram(df, x=df.columns[0], title=f'histograma de {df.columns[0]}')
    st.plotly_chart(fig, use_container_width=True)

# Boton para contruir un grafico de dispersion
if st.button("construir Scatter Plot"):
    st.write("Grafico de dispersion: Precio vs Odometro")
    if 'odometer' in df.columns and 'price' in df.columns:
        fig2 = px.scatter(df, x='odometer', y='price', title='Precio vs Odometro')
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.write("las mcolumnas necesarias para el scatter plot no estan disponibles.") 

# Botón para construir un gráfico circular
if st.button("Construir gráfico circular"):
    st.write("Gráfico circular sobre las condiciones de los vehículos")
    if 'condition' in df.columns:
        fig3 = px.pie(df, names='condition', title='Distribución de Condiciones de los Vehículos')
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.write("La columna 'condition' no está disponible en los datos.")
            