from pydantic import BaseModel

class Movie(BaseModel):
    name: str
    year: int
    genre: str
    rating: float