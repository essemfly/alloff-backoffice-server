FROM python:3.10

USER root
RUN apt-get update \
    && apt-get --yes install apt-utils \
    && apt-get --yes install curl

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
ENV PATH "/root/.local/bin:$PATH"
COPY . /office