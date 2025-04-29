from app.adapters.kinopoisk_adapter import KinopoiskAdapter

class MovieService:
    def __init__(self, kinopoisk_adapter: KinopoiskAdapter):
        self.kinopoisk_adapter = kinopoisk_adapter

    def rank_movies_by_genre_match(self, movies, recommended_genres):
        ranked_movies = []
        for movie in movies:
            movie_genres = set([name.name for name in movie.genres])
            match_count = len(movie_genres.intersection(recommended_genres))
            ranked_movies.append((movie, match_count))
        ranked_movies.sort(key=lambda x: x[1], reverse=True)
        return [
            {'name': movie[0].name, 'description': movie[0].description} 
            for movie in ranked_movies
        ]

    def recommend_movies(self, genres):
        movies = self.kinopoisk_adapter.find_movies_by_genres(genres)
        print(movies)
        return self.rank_movies_by_genre_match(movies, set(genres))
