FROM python:3.9.2-slim-buster

RUN pip install poetry==1.1.5

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-dev --no-interaction --no-ansi

COPY fakeit /app/fakeit
COPY example.json /app/
CMD ["poetry", "run", "python", "fakeit/main.py", "example.json"]