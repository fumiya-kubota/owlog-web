FROM python:3.7.0

WORKDIR /app

RUN pip install pipenv
COPY app/Pipfile .
COPY app/Pipfile.lock .

RUN pipenv install --system --deploy

COPY app .

ENTRYPOINT ["python", "owlog/main.py"]
