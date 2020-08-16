# django-blogproject

 Based on the Python 3.6.x

Exercise [HelloDjango - Django博客教程（第二版）](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/)  from [追梦人物的博客](https://www.zmrenwu.com/)

## Installation

clone:

```bash
$ git clone https://github.com/HEY-BLOOD/watchlist.git
$ cd blogproject
```

create & active virtual environment then install dependencies:

```bash
$ python -m venv env
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

migrate database & create superuser:

```bash
$ python manage.py migrate
$ python manage.py createsuperuser
```

## Run

run by default:

```bash
$ python manage.py runserver
```

## Access

access url http://127.0.0.1:8000 in a browser

