clone the project

```console
cd plenario
```

setup for flask
```console
pip install -r requirements.txt
```

create a `DATABASE_URL` envvar with the database credentials, for example:
```
export DATABASE_URL=sqlite:///db.sqlite3
```

to fully run the project:
```console
python run.py
```

run migrations
```console
python manage.py db migrate
```