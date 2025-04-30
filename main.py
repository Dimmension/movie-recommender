from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.models.emotion_model import EmotionModel
from app.services.emotion_service import EmotionService
from app.adapters.kinopoisk_adapter import KinopoiskAdapter
from app.services.movie_service import MovieService
import uvicorn

app = FastAPI()

emotion_model = EmotionModel()
emotion_service = EmotionService(emotion_model)
kinopoisk_adapter = KinopoiskAdapter(token="K5MH51Y-QZM4QQ6-NH5XJA4-MYFY25T")
movie_service = MovieService(kinopoisk_adapter)


class TextRequest(BaseModel):
    text: str


@app.post("/recommend/")
async def recommend(request: TextRequest):
    try:
        text = request.text.strip()
        if not text:
            raise HTTPException(status_code=400, detail="Text cannot be empty.")

        recommended_genres, emotions = emotion_service.recommend_genres(text)
        top_movies = movie_service.recommend_movies(recommended_genres)
        return {
            "text": text,
            "emotions": emotions,
            "recommended_genres": recommended_genres,
            "top_movies": top_movies,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
