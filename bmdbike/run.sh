rm -f db.sqlite3
python manage.py migrate
python manage.py runserver
