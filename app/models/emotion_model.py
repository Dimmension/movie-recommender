import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class EmotionModel:
    def __init__(
        self,
        model_name="fyaronskiy/deepvk_deberta-v1-base__bs32_max_len128_ep10_lr5e-05_lr_sheduler_linear",
    ):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)

        self.best_thresholds = [
            0.5510204081632653,
            0.18367346938775508,
            0.1020408163265306,
            0.1020408163265306,
            0.18367346938775508,
            0.22448979591836732,
            0.2040816326530612,
            0.4081632653061224,
            0.2040816326530612,
            0.22448979591836732,
            0.24489795918367346,
            0.3061224489795918,
            0.16326530612244897,
            0.2857142857142857,
            0.3877551020408163,
            0.32653061224489793,
            0.02040816326530612,
            0.16326530612244897,
            0.44897959183673464,
            0.1020408163265306,
            0.22448979591836732,
            0.04081632653061224,
            0.12244897959183673,
            0.061224489795918366,
            0.14285714285714285,
            0.42857142857142855,
            0.3061224489795918,
            0.26530612244897955,
        ]
        self.LABELS = [
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

    def predict_emotions(self, text):
        inputs = self.tokenizer(
            text,
            truncation=True,
            add_special_tokens=True,
            max_length=128,
            return_tensors="pt",
        )
        with torch.no_grad():
            logits = self.model(**inputs).logits
        probas = torch.sigmoid(logits).squeeze(dim=0)
        class_binary_labels = (probas > torch.tensor(self.best_thresholds)).int()
        return [
            self.LABELS[label_id]
            for label_id, value in enumerate(class_binary_labels)
            if value == 1
        ]
