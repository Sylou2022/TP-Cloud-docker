FROM python:3.11

ENV APP_HOME /app
WORKDIR $APP_HOME

RUN apt-get update
COPY requirement .

RUN pip install -r requirement

COPY . .

CMD ["python3", "app.py"]