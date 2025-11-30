from fastapi import FastAPI
from api.movies import MovieAPI

app = FastAPI()

movie_api = MovieAPI()

@app.get("/movies")
def search_movies(name: str):
    return movie_api.search_movies(name)

@app.post("/movies")
def add_movie(name: str, year: int, genre: str, rating: float):
    return movie_api.add_movie(name, year, genre, rating)