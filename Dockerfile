FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN python -m pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system
COPY . /code/
