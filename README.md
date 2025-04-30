# movie-recommender
Проект по дисциплине "Технологии разработки веб-приложений"


### Запрос
```
curl -X POST "http://127.0.0.1:8000/recommend/" -H "Content-Type: application/json" -d '{"text": "Я чувствую радость и любовь!"}'
```

### Build
```
docker build -t my-base-image -f Dockerfile.base .
docker build -t my-app -f Dockerfile.app .
```

### Run
```
docker run -p 8000:8000 my-app
```

### Run tests
```
PYTHONPATH=. pytest --cov=app
```