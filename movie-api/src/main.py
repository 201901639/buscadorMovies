import streamlit as st
import pandas as pd
from services.excel_service import ExcelService

excel_service = ExcelService(
    r"C:\Users\silvi\OneDrive - Universidad Pontificia Comillas\Documentos de interés\cosas mías\proyecto movie\movie-api\src\data\peliculas.xlsx"
)

# Obtener géneros únicos del Excel
all_movies = excel_service.get_movies()
unique_genres = sorted({m["genre"] for m in all_movies if m.get("genre")})

st.title("Gestor de Películas")

# Buscar películas
st.header("Buscar películas")
year = st.number_input("Año", min_value=1900, max_value=2100, step=1, value=2025)
genre = st.selectbox("Género", options=[""] + unique_genres)

if st.button("Buscar"):
    movies = excel_service.get_movies()
    if year:
        movies = [m for m in movies if m["Año"] == year]
    if genre:
        movies = [m for m in movies if m["genre"].lower() == genre.lower()]
    if movies:
        st.dataframe(pd.DataFrame(movies))
    else:
        st.info("No se encontraron películas con esos criterios.")

# Añadir película
st.header("Añadir nueva película")
with st.form("add_movie"):
    name = st.text_input("Nombre")
    year_new = st.number_input("Año", min_value=1900, max_value=2100, step=1)
    genre_new = st.selectbox("Género", options=unique_genres)
    rating = st.number_input("Nota", min_value=0.0, max_value=10.0, step=0.1)
    submitted = st.form_submit_button("Añadir")
    if submitted:
        excel_service.add_movie(name, int(year_new), genre_new, rating)
        st.success("Película añadida correctamente")