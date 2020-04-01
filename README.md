# Varchas ![Status active](https://img.shields.io/badge/Status-active%20development-2eb3c1.svg) ![Django 3.0.0](https://img.shields.io/badge/Django-3.0.0-green.svg) ![Python 3.7.1](https://img.shields.io/badge/Python-3.7.1-blue.svg)

## Main web portal for the annual sports fest of IIT Jodhpur Varchas.
### Installation:
Requirements:
- Python 3.7.1 runtime
- Django 3.0.0
- Other dependencies in `requirements.txt`

Procedure:
- Install [python](https://www.python.org/downloads/) in your environment(pre-installed on Ubuntu).
- Navigate to the cloned repository.
    ```
    cd <project_directory_name>     # intern
    ```
- Install `pipenv` for dependency management
    ```
    pip install pipenv
    ```
- Use pip to install other dependencies from `requirements.txt`
    ```
    pip install -r requirements.txt
    ```

- Optionally activate virtual environment, if you don't want to activate env, use `pipenv run` to run python scripts
    ```
    source "$(pipenv --venv)"/bin/activate
    ```
- Make database migrations
    ``` 
    python manage.py makemigrations
    python manage.py migrate
    ```
- Create a superuser
    ```
    python manage.py createsuperuser 
    ```
- Run development server on localhost
    ```
    python manage.py runserver 
    ```

