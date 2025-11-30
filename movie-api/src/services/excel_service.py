import pandas as pd

class ExcelService:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_movies(self):
        df = pd.read_excel(self.file_path)
        movies = df.to_dict(orient='records')
        return movies

    def add_movie(self, name, year, genre, rating):
        df = pd.read_excel(self.file_path)
        new_movie = {
            "Nombre": name,
            "Año": year,
            "genre": genre,
            "Nota": rating
        }
        df = pd.concat([df, pd.DataFrame([new_movie])], ignore_index=True)
        df.to_excel(self.file_path, index=False)

excel_service = ExcelService(
    "data/peliculas.xlsx"
)