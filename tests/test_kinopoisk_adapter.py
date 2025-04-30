import pytest
from unittest.mock import MagicMock
from app.models.emotion_model import EmotionModel
from app.services.emotion_service import EmotionService


@pytest.fixture
def mock_emotion_model():
    model = MagicMock(spec=EmotionModel)
    model.predict_emotions.return_value = ["joy", "love"]
    return model


@pytest.fixture
def emotion_service(mock_emotion_model):
    return EmotionService(emotion_model=mock_emotion_model)


def test_recommend_genres(emotion_service):
    text = "Я чувствую радость и любовь!"
    genres, emotions = emotion_service.recommend_genres(text)

    assert isinstance(genres, list)
    assert isinstance(emotions, list)

    assert emotions == ["joy", "love"]

    expected_genres = set(
        EmotionService.EMOTION_TO_GENRES["joy"]
        + EmotionService.EMOTION_TO_GENRES["love"]
    )
    assert set(genres) == expected_genres
