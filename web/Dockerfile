FROM python:3.7.0

WORKDIR /app

RUN pip install pipenv

COPY app .
RUN pipenv install --system --deploy

ENTRYPOINT ["python", "owlog/main.py"]
