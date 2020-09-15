# django-blogproject

 Based on the Python 3.6.x

Learn [HelloDjango - Django博客教程（第二版）](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/)  from [追梦人物的博客](https://www.zmrenwu.com/)

## Installation

clone:

```bash
$ git clone https://github.com/HEY-BLOOD/django-blogproject.git
$ cd django-blogproject
```

create & active virtual environment then install dependencies:

```bash
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```

migrate database & create virtual data:

```bash
$ python manage.py migrate
$ python -m scripts.fake
```

## Run

run by default:

```bash
$ python manage.py runserver 0.0.0.0:8000
```

access http://127.0.0.1:8000 in a browser

