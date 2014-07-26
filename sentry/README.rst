Sentry
======

By Micah Denbraver

Setup
-----

For this demo you can install requirements from requirements.txt:

    pip install -r requirements.txt

To set up sentry with your own project, look to the links below.

Setup Sentry
^^^^^^^^^^^^

http://sentry.readthedocs.org/en/latest/quickstart/index.html#install-sentry

Configure Raven
^^^^^^^^^^^^^^^

http://raven.readthedocs.org/en/latest/config/django.html

\- or -

http://raven.readthedocs.org/en/latest/config/logging.html


Run
---

Start Sentry
^^^^^^^^^^^^

    sentry --config=sentry.conf.py migrate
    sentry --config=sentry.conf.py createsuperuser
    sentry --config=sentry.conf.py runserver

Start Demo App
^^^^^^^^^^^^^^

    python manage.py runserver

Example URL's
^^^^^^^^^^^^^

http://localhost:8080/exception-demo/

http://localhost:8080/logging-demo/
