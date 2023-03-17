ARG registry=test
# FROM fukouhei001/opencv-python10:v1
FROM ${registry}/opencv-python3-10:v1
# FROM ${registry}/opencv-python3-8:v1
WORKDIR /myapp
COPY ./ ./

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install build-essential -y
RUN apt-get install git -y
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org/  | python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

RUN poetry install --no-root

# ENV http_proxy=
# ENV https_proxy=

EXPOSE 80

CMD ["python", "./main.py"]
# CMD ["python", "./main_prod.py"]
