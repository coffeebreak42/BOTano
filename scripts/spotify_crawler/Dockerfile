FROM python:3.7.4-alpine3.10

COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./src/main.py"] 
COPY src src