# thinkster-django-angular
Building out the Not Google Plus app from scratch using latest versions of Django, DRF, Angular.
https://thinkster.io/django-angularjs-tutorial

## Setting up
* git clone https://github.com/sgallen/thinkster-django-angular.git
* virtualenv --verbose -p /opt/python3.4/bin/python3 ~/Envs/thinkster
* . ~/Envs/thinkster/bin/activate
* pip install -r requirements/dev.txt
* createdb -U postgres django_base
* python manage.py migrate
* python manage.py runserver
    * http://localhost:8000/foo
