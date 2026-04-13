FROM python:3.9

WORKDIR /app

COPY random_number.py  /app

CMD ["python","random_number"]
