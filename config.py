import environ
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, ['*']),
)

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env('ALLOWED_HOSTS')
DB_NAME = env('DB_NAME')
DB_USER = env('DB_USER')
DB_PORT = env('DB_PORT')
DB_HOST = env('DB_HOST')
DB_PASSWORD = env('DB_PASSWORD')
