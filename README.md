# Visualización de Datos de Vehículos con Streamlit

Esta aplicación web interactiva, desarrollada con **Streamlit**, permite a los usuarios explorar y visualizar datos relacionados con anuncios de vehículos usados de manera fácil e intuitiva.

## Propósito del Proyecto

El objetivo principal de esta aplicación es ofrecer una herramienta amigable para analizar datos de vehículos usados. A través de gráficos interactivos, los usuarios pueden explorar métricas clave, como el **kilometraje** (`odometer`) y el **precio** (`price`), facilitando la identificación de tendencias y patrones en el conjunto de datos.

## Funcionalidades

- **Visualización de primeros datos**: Muestra las primeras cinco filas del conjunto de datos, proporcionando un vistazo inicial a la información disponible.
- **Histograma del kilometraje**: Presenta la distribución del kilometraje de los vehículos anunciados, lo que permite observar rangos y frecuencias comunes.
- **Gráfico de dispersión**: Ilustra la relación entre el kilometraje y el precio de los vehículos, ayudando a identificar posibles correlaciones.
- **Filtros personalizados**:
  - Selección por **precio**, **kilometraje** y **tipo de combustible**.
  - Con base en los filtros aplicados:
    - Genera un gráfico de dispersión **Precio vs Kilometraje por Tipo de Combustible**.
    - Crea un gráfico de distribución por **Tipo de Combustible**.

## Tecnologías utilizadas

- **Frontend**: Streamlit.
- **Backend**: Python (pandas,plotly expres).
- **Dataset**: Datos de anuncios de vehículos usados en formato CSV.

## Link de Render.com
- https://vehicles-vl5n.onrender.com