import os

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.pardir)

SECRET_KEY = 'dqkkdmfkwef45knngjfngnjgk'
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}


INSTALLED_APPS = ('no_delete', 'tests',)
