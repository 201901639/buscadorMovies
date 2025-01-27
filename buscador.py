import pandas as pd
import streamlit as st

# Leer la base de datos
movies_DEF = pd.read_csv("generadorBBDD/Movies_DEF.csv", encoding='utf-8')

# Limpiar datos si es necesario
movies_DEF['Movie or Series'] = movies_DEF['Movie or Series'].str.replace('Ã', '').str.strip()
movies_DEF['Category'] = movies_DEF['Category'].str.strip()

# Configurar la app de Streamlit
st.title("Buscador de Películas y Series")
st.subheader("Explora fácilmente las películas y series de la base de datos")

# Campo de búsqueda
search_term = st.text_input("Buscar por título, categoría o año:")

# Filtrar datos según el término de búsqueda
if search_term:
    filtered_data = movies_DEF[
        movies_DEF.apply(lambda row: search_term.lower() in str(row.values).lower(), axis=1)
    ]
    st.write(f"Se encontraron {len(filtered_data)} resultados:")
    st.dataframe(filtered_data)
else:
    st.write("Introduce un término de búsqueda para comenzar.")

# Mostrar todos los datos si no hay búsqueda activa
st.write("Base de datos completa:")
st.dataframe(movies_DEF)