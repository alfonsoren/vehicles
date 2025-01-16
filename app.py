

# Importamos las bibliotecas necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# Contenido de la aplicación basada en Streamlit
st.header("Datos de los vehículos")

# Mostrar una vista previa de los datos
if st.checkbox("Mostrar los primeros registros del conjunto de datos"):
    st.write('Primeros 5 datos')
    st.write(car_data.head())

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

# Filtros dinámicos
st.sidebar.header("Filtros")
price_min, price_max = st.sidebar.slider(
    "Selecciona el rango de precios ($)", 
    min_value=int(car_data['price'].min()), 
    max_value=int(car_data['price'].max()), 
    value=(int(car_data['price'].min()), int(car_data['price'].max()))
)

mileage_max = st.sidebar.slider(
    "Selecciona el kilometraje máximo (millas)", 
    min_value=int(car_data['odometer'].min()), 
    max_value=int(car_data['odometer'].max()), 
    value=int(car_data['odometer'].max())
)

fuel_type = st.sidebar.multiselect(
    "Selecciona el tipo de combustible", 
    options=car_data['fuel'].unique(), 
    default=car_data['fuel'].unique()
)

# Aplicar filtros al DataFrame
filtered_data = car_data[
    (car_data['price'] >= price_min) & 
    (car_data['price'] <= price_max) & 
    (car_data['odometer'] <= mileage_max) & 
    (car_data['fuel'].isin(fuel_type))
]

# Mostrar el DataFrame filtrado
st.write(f"Resultados filtrados: {filtered_data.shape[0]} vehículos encontrados.")
st.write(filtered_data)

# Gráficos interactivos
st.subheader("Visualizaciones basadas en los filtros aplicados")

# Gráfico de dispersión: precio vs kilometraje
scatter_fig = px.scatter(
    filtered_data, 
    x="odometer", 
    y="price", 
    color="fuel", 
    title="Precio vs Kilometraje por Tipo de Combustible",
    labels={"odometer": "Kilometraje (millas)", "price": "Precio ($)"},
    hover_data=["model_year", "model"]  # Reemplaza 'year' con 'model_year'
)
st.plotly_chart(scatter_fig, use_container_width=True)

# Gráfico de barras: distribución de tipos de combustible
fuel_data = filtered_data['fuel'].value_counts().reset_index(name='fuel_count')
fuel_data.columns = ['fuel', 'fuel_count']  # Renombramos las columnas

bar_fig = px.bar(
    fuel_data,
    x='fuel',  
    y='fuel_count',
    title="Distribución de Vehículos por Tipo de Combustible",
    labels={'fuel': 'Tipo de Combustible', 'fuel_count': 'Cantidad de Vehículos'},
    color='fuel_count'
)
st.plotly_chart(bar_fig, use_container_width=True)