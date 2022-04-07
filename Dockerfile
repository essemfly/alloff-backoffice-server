FROM python:3.10-slim-buster
RUN apt-get update
RUN apt-get install git -y
RUN pip install poetry
WORKDIR /server
COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0:8000"]
EXPOSE 8000
