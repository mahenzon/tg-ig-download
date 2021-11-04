FROM python:3.9-buster

WORKDIR /app

RUN pip install -U pip poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
# TODO: --no-dev ?
RUN poetry install

COPY . .

RUN chmod +x entrypoint.sh
ENTRYPOINT . ./entrypoint.sh
CMD python webhook.py
