# pull official base image
FROM python:3.8.3-alpine

# set secret key and postgres args
ARG secret_key
ENV SECRET_KEY=$secret_key

ARG postgres_username
ENV POSTGRES_USERNAME=$postgres_username

ARG postgres_password
ENV POSTGRES_PASSWORD=$postgres_password

ARG postgres_host
ENV POSTGRES_HOST=$postgres_host

RUN echo $POSTGRES_HOST
RUN echo $postgres_host
RUN echo $POSTGRES_USERNAME
RUN echo $postgres_username

# set work directory
WORKDIR /allidrett

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependenciesUN \
RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN apk --purge del .build-deps

# copy project
COPY . .

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
RUN chmod +x ./scripts/start.sh
EXPOSE 8000

ENTRYPOINT [ "./scripts/start.sh" ]