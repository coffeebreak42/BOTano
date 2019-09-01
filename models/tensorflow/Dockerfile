FROM tensorflow/tensorflow:latest-gpu-py3

WORKDIR /app

ARG data
ADD $data /data/

CMD ["python", "./src/main.py"]

COPY src src