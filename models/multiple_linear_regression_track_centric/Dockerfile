FROM reportbee/datascience:latest

WORKDIR /app

RUN mkdir /app/images/

ARG data
ADD $data /data/

CMD ["python3", "./src/main.py"]

COPY src src