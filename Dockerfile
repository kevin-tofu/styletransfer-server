ARG registry=test
# FROM fukouhei001/opencv-python10:v1
# FROM ${registry}/opencv-python3-10:v1
FROM ${registry}/opencv-python3-8:v1

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install build-essential -y
RUN apt-get install git -y
# RUN apt install -y ffmpeg

WORKDIR /myapp
COPY ./ ./
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ENV http_proxy=
# ENV https_proxy=

EXPOSE 80

CMD ["python", "./main.py"]
# CMD ["python", "./main_prod.py"]
