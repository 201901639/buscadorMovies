import pandas as pd

class ExcelService:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_movies(self):
        df = pd.read_excel(self.file_path)
        movies = df.to_dict(orient='records')
        return movies

    def add_movie(self, name, year, genre, rating):
        new_movie = {
            'Name': name,
            'Year': year,
            'Genre': genre,
            'Rating': rating
        }
        df = pd.read_excel(self.file_path)
        df = df.append(new_movie, ignore_index=True)
        df.to_excel(self.file_path, index=False)