web: gunicorn config.wsgi:application
worker: celery worker --app=bila.taskapp --loglevel=info
