release: python manage.py migrate 
web: uvicorn API:app --reload
web: gunicorn API:app