import pandas as pd
import plotly.express as px
import streamlit as st


df = pd.read_csv('../../datasets/vehicles_us.csv')


# Encabezado de la apalicacion
st.header('ANALISIS EXPLORATORIO DE DATOS DE VEHICULOS')
# Boton para contruir un histograma
if st.button('Construir histograma'):
     st.write("Histograma de la columna  'odometer'")
     if 'odometer' in df.columns:
            fig = px.histogram(df, x='odometer', title='histograma de odometro')
     else:
            fig = px.histogram(df, x=df.columns[0], title=f'histograma de  {df.columns[0]}')
    st.plotly_chart(fig, use_container_width=True)

# Boton para contruir un grafico de dispersion
if st.button("construir Scatter Plot"):
     st.write("Grafico de dispersion: Precio vs Odometro")
     if 'odometer' in df.columns and 'price', title='Precio vs Odometro')
         fig2 = px.scatter(df, x='odometer', y='price', title='Precio vs Odometro')
         st.plotly_chart(fig2, use_container_width=True)
    else:
        st.write("las mcolumnas necesarias para el scatter plot no estan disponibles.") 

            