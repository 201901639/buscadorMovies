import pandas as pd
import streamlit as st

# Leer la base de datos
movies_DEF = pd.read_csv("generadorBBDD/Movies_DEF.csv", encoding='utf-8')

# Limpiar datos si es necesario
movies_DEF['Movie or Series'] = movies_DEF['Movie or Series'].str.replace('Ã', '').str.strip()
movies_DEF['Category'] = movies_DEF['Category'].str.strip()

# Configuración de la app de Streamlit
st.set_page_config(page_title="Buscador de Películas y Series", layout="wide", page_icon="🎬")

# Estilos personalizados (fuentes y colores)
st.markdown("""
    <style>
        body {
            font-family: 'Netflix Sans', Arial, sans-serif;
        }
        h1 {
            text-align: center;
            color: #E50914;
            font-size: 50px;
        }
        h3 {
            text-align: center;
            color: #B3B3B3;
            font-size: 30px;
        }
        .search-bar {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        .table {
            margin-left: auto;
            margin-right: auto;
        }
    </style>
    """, unsafe_allow_html=True)

# Título y subtítulo
st.markdown("""
    <h1>Buscador de Películas y Series</h1>
    <h3>Buscador de pelis buenas para la familia</h3>
    """, unsafe_allow_html=True)

# Campo de búsqueda (centrado)
search_term = st.text_input("Buscar por título, categoría o año:", key="search", label_visibility="collapsed")

# Filtrar los datos según el término de búsqueda
if search_term:
    filtered_data = movies_DEF[
        movies_DEF.apply(lambda row: search_term.lower() in str(row.values).lower(), axis=1)
    ]
    st.markdown(f"### Se encontraron {len(filtered_data)} resultados:", unsafe_allow_html=True)
    st.dataframe(filtered_data, use_container_width=True, key="result_table")
else:
    st.write("Introduce un término de búsqueda para comenzar.")

# Agregar una sección visual para mostrar todos los datos si no hay búsqueda activa
st.markdown("### Base de datos completa:", unsafe_allow_html=True)
st.dataframe(movies_DEF, use_container_width=True)