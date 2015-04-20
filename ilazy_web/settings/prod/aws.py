import dj_database_url

from ilazy_web.settings.base import *


DEBUG = os.environ.get('DEBUG') == 'True'

DATABASES = {
    'default': {
        'ENGINE': os.environ['RDS_DB_ENGINE'],
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
    }
}

ALLOWED_HOSTS = ['*']

ADMINS = (('Bang', 'daotranbang@gmail.com'), )
