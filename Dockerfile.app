FROM my-base-image

COPY . .

CMD ["python3", "main.py"]