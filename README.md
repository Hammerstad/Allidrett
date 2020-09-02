# Allidrett

![Main](https://github.com/Hammerstad/Allidrett/workflows/Main/badge.svg)

Påmeldingsside for allidrett til Nidelv IL, ettersom den eksisterende løsningen fungerer heller dårlig (ikke outsource ting til India...).

Påtenkte features:
 - Påmelding
 - Admin grensesnitt
 - Flere grupper
 - Noe mail-sending
 - GDPR *sigh*

## Utviklingsmiljø

Vi bruker python 3, og ikke 2. Om du har python2 som default (kjør `python --version` for å sjekke), bytt ut alle `python` kommandoer med `python3`. Det samme gjelder `pip` som blir `pip3`.

Det kreves også virtualenv:

```
pip install virtualenv
```

Opprett et virtualenv, aktiver det og installer requirements:

```
# Opprett et virtual environment i mappen "venv"
virtualenv venv
# Aktiver det
source venv/bin/activate
# Installer alle requirements. Disse havner i venv mappa
pip install -r requirements.txt
```

Nå kan du synce databasen, og kjøre:

```
python manage.py migrate
python manage.py runserver
```

Nå kjører utviklingsserver lokalt, og du kan nå siden på http://localhost:8000

Have fun :)

## Building and running dockerfile locally

Example, paste correct values for credentials

    docker build --no-cache \
        --build-arg secret_key="abcdefghijklmnop" \
        --build-arg postgres_username="user" \
        --build-arg postgres_host="host" \
        --build-arg postgres_password="password" \
        -t hammerstad/allidrett .
    docker run -p 8000:8000 hammerstad/allidrett