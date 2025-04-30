from app.models.emotion_model import EmotionModel


class EmotionService:
    EMOTION_TO_GENRES = {
        "admiration": ["биография", "история", "драма", "военный"],
        "amusement": ["комедия", "мультфильм", "аниме"],
        "anger": ["боевик", "криминал", "триллер"],
        "annoyance": ["драма", "реальное ТВ", "ток-шоу"],
        "approval": ["драма", "биография", "история"],
        "caring": ["мелодрама", "семейный", "драма"],
        "confusion": ["детектив", "фантастика", "фэнтези"],
        "curiosity": ["детектив", "фантастика", "приключения"],
        "desire": ["мелодрама", "романтика", "драма"],
        "disappointment": ["драма", "реальное ТВ", "ток-шоу"],
        "disapproval": ["драма", "криминал", "фильм-нуар"],
        "disgust": ["ужасы", "криминал", "драма"],
        "embarrassment": ["комедия", "мультфильм", "аниме"],
        "excitement": ["боевик", "приключения", "фантастика"],
        "fear": ["ужасы", "триллер", "детектив"],
        "gratitude": ["драма", "биография", "история"],
        "grief": ["драма", "мелодрама", "биография"],
        "joy": ["комедия", "мюзикл", "аниме"],
        "love": ["мелодрама", "романтика", "драма"],
        "nervousness": ["триллер", "детектив", "ужасы"],
        "optimism": ["комедия", "приключения", "аниме"],
        "pride": ["биография", "история", "драма"],
        "realization": ["драма", "биография", "история"],
        "relief": ["комедия", "мультфильм", "аниме"],
        "remorse": ["драма", "биография", "история"],
        "sadness": ["драма", "мелодрама", "биография"],
        "surprise": ["фантастика", "фэнтези", "приключения"],
        "neutral": ["документальный", "реальное ТВ", "новости"],
    }

    def __init__(self, emotion_model: EmotionModel):
        self.emotion_model = emotion_model

    def recommend_genres(self, text):
        emotions = self.emotion_model.predict_emotions(text)
        recommended_genres = set()
        for emotion in emotions:
            if emotion in self.EMOTION_TO_GENRES:
                recommended_genres.update(self.EMOTION_TO_GENRES[emotion])
        print(list(recommended_genres), emotions)
        return list(recommended_genres), emotions
