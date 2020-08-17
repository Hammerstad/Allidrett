# Allidrett

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
python allidrett/manage.py migrate
python allidrett/manage.py runserver
```

Nå kjører utviklingsserver lokalt, og du kan nå siden på http://localhost:8000

Have fun :)