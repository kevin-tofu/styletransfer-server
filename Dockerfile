# ARG registry=test
# FROM python:3.10.12-bookworm
FROM python:3.10.12-slim-bookworm
# FROM ${registry}/opencv-python3-10:v1

WORKDIR /myapp
COPY ./pyproject.toml ./pyproject.toml

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install build-essential -y
RUN apt-get install curl git -y

ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org/  | python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

RUN poetry install --no-root

COPY ./ ./
# ENV http_proxy=
# ENV https_proxy=

EXPOSE 80

CMD ["python", "./src/main.py"]
