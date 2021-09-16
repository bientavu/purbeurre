# Purbeurre

Purbeurre is a web-app that will allow you search for an unhealthy product and then some healthy substitute products will be proposed.
You will be able to create an account and save the product into favorites.
It is based on the Openfoodfact database, on the nutriscore.

## **Prerequisites**
- Python 3.8
- Django 3.2.7
- PostGreSQL (create a database)
- Others required modules are in the pipfile

## **How to install**
- `git clone https://github.com/bientavu/purbeurre.git`
- `cd purbeurre/`
- `pipenv install`
- `pipenv shell` (if not already activated)

In purbeurre/settings.py :
1. Update the "SECRET_KEY" to a random key
2. Update the database name to yours
3. Update the database password to yours

- `python manage.py migrate`
- `python manage.py db_insertion`
- `python manage.py runserver`

You can check the app at http://127.0.0.1:8000/

## **My app**
