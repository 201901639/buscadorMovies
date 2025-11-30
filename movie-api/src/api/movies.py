from fastapi import APIRouter, HTTPException
from services.excel_service import ExcelService
from models.movie import Movie
from typing import List

router = APIRouter()
excel_service = ExcelService()

@router.get("/movies", response_model=List[Movie])
def search_movies(year: int = None, genre: str = None):
    movies = excel_service.get_movies()
    if year:
        movies = [movie for movie in movies if movie.year == year]
    if genre:
        movies = [movie for movie in movies if movie.genre.lower() == genre.lower()]
    return movies

@router.post("/movies", response_model=Movie)
def add_movie(movie: Movie):
    try:
        excel_service.add_movie(movie)
        return movie
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))