### STARTING A NEW DJANGO PROJECT

Asuming you created an empty workspace folder and you created a virtualenv and installed django, Run the command below

```bash
django-admin.py startproject project .
```

The command above starts a new django project inside of the workspace folder.

### RUNNING INITIAL MIGRATIONS

```bash
python manage.py migrate # Creates initial database tables
```

### CREATING DAJANGO APP

```bash
python manage.py startapp home
```

### Queryset API

- Model.objects.create # Create new item in database table
- Model.objects.get # Retrive single item from database table
- Model.objects.all # Get all items in the database table
