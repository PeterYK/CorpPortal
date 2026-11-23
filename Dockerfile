# Запуск контейнера:
# docker build -t my-django .
# docker run -p 8000:8000 my-django
 
FROM python:3.12-slim
 
WORKDIR /app
 
RUN pip install --no-cache-dir poetry
 
COPY pyproject.toml poetry.lock* ./
 
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --only main
 
COPY . .
 
EXPOSE 8000
 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
