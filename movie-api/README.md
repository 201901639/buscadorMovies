# Movie API

This project is a simple API for managing a list of movies stored in an Excel file. It allows users to search for movies by various attributes and add new movies to the list.

## Project Structure

```
movie-api
├── src
│   ├── main.py              # Entry point of the application
│   ├── api
│   │   └── movies.py        # API routes for movie operations
│   ├── services
│   │   └── excel_service.py  # Service for handling Excel file operations
│   ├── models
│   │   └── movie.py         # Movie model definition
│   └── data
│       └── peliculas.xlsx    # Excel file containing movie data
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd movie-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage

### Searching for Movies

To search for movies, send a GET request to the following endpoint:

```
GET /movies?name=<movie_name>&year=<year>&genre=<genre>&rating=<rating>
```

### Adding a New Movie

To add a new movie, send a POST request to the following endpoint with the movie details in the request body:

```
POST /movies
```

**Request Body:**
```json
{
    "name": "Movie Title",
    "year": 2023,
    "genre": "Genre",
    "rating": 8.5
}
```

## License

This project is licensed under the MIT License.