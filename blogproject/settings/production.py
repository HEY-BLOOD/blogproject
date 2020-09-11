from .common import *
import os

#Read secret key from a file
with open(os.path.join(BASE_DIR, 'django_secrect_key.txt')) as f:
    SECRET_KEY = f.read().strip()

DEBUG = False
ALLOWED_HOSTS = ['*']
