import pytest
from app.models.emotion_model import EmotionModel


@pytest.fixture
def emotion_model():
    return EmotionModel()


def test_predict_emotions(emotion_model):
    text = "Я чувствую радость и любовь!"
    emotions = emotion_model.predict_emotions(text)

    assert isinstance(emotions, list)

    valid_labels = [
        "admiration",
        "amusement",
        "anger",
        "annoyance",
        "approval",
        "caring",
        "confusion",
        "curiosity",
        "desire",
        "disappointment",
        "disapproval",
        "disgust",
        "embarrassment",
        "excitement",
        "fear",
        "gratitude",
        "grief",
        "joy",
        "love",
        "nervousness",
        "optimism",
        "pride",
        "realization",
        "relief",
        "remorse",
        "sadness",
        "surprise",
        "neutral",
    ]
    for emotion in emotions:
        assert emotion in valid_labels
