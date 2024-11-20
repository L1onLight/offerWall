## Server startup

### Python 3.12 is required

### Install dependencies

```bash
pip install -r requirements.txt
```

### After db initialization (only once)

```bash
python manage.py migrate
```

### Start server

```bash
python manage.py runserver
```

### Docs

[Swagger](http://127.0.0.1:8000/api/swagger/)