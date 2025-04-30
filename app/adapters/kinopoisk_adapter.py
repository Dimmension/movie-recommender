from kinopoisk_dev import KinopoiskDev, MovieParams, MovieField, PossValField


class KinopoiskAdapter:
    def __init__(self, token: str):
        self.kp = KinopoiskDev(token=token)

    def find_movies_by_genres(self, genres, limit=1):
        movies = []
        for genre in genres:
            params = [
                MovieParams(keys=PossValField.GENRES, value=genre),
                MovieParams(keys=MovieField.LIMIT, value=limit),
            ]
            try:
                movies.append(self.kp.find_many_movie(params=params).docs[0])
            finally:
                continue
        return movies
