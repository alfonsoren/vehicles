# Importamos las bibliotecas necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# Contenido de la aplicación basada en Streamlit
st.header("Datos de los vehículos")

# Casillas de verificación para seleccionar el gráfico
show_histogram = st.checkbox('Mostrar histograma')
show_scatterplot = st.checkbox('Mostrar gráfico de dispersión')

# Mostrar el histograma si la casilla está marcada
if show_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer", title="Histograma del Odómetro")
    st.plotly_chart(fig, use_container_width=True)

# Mostrar el gráfico de dispersión si la casilla está marcada
if show_scatterplot:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos')
    scatter_fig = px.scatter(
        car_data, 
        x="odometer", 
        y="price", 
        title="Relación entre el odómetro y el precio", 
        labels={"odometer": "Kilometraje (millas)", "price": "Precio (USD)"}
    )
    st.plotly_chart(scatter_fig, use_container_width=True)
