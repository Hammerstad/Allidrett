# pull official base image
FROM python:3.8.3-alpine

# set secret key
ARG secret_key
ENV SECRET_KEY=$secret_key

# set work directory
WORKDIR /allidrett

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
RUN chmod +x ./scripts/start.sh
EXPOSE 8000

ENTRYPOINT [ "./scripts/start.sh" ]