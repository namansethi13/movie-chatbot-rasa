FROM rasa/rasa-sdk:3.6.0

WORKDIR /app

COPY actions/requirements.txt ./

USER root

COPY ./actions /app/actions

COPY .env ./

RUN pip install -r requirements.txt

USER 1000

