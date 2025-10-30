services:
  - type: web
    name: django
    env: python
    plan: free
    buildCommand: |
      pip install -r requirements.txt
      python manage.py migrate
      python manage.py collectstatic --noinput
    startCommand: gunicorn reseau_entrepreneurs.wsgi
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: reseau_entrepreneurs.settings
