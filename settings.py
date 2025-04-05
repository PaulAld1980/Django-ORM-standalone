from environs import Env

env = Env()    # Создаём объект Env для работы с переменными окружения

env.read_env()    # Загружаем переменные из .env файла

DATABASES = {    # Настройки базы данных с валидацией типов
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env.str('DB_HOST'),  # Строка, обязательная переменная
        'PORT': env.int('DB_PORT', default=5432),  # Целое число, значение по умолчанию 5432
        'NAME': env.str('DB_NAME'),  # Строка, обязательная переменная
        'USER': env.str('DB_USER'),  # Строка, обязательная переменная
        'PASSWORD': env.str('DB_PASSWORD'),  # Строка, обязательная переменная
    }
}

INSTALLED_APPS = ['datacenter']    # Список установленных приложений

SECRET_KEY = env.str('SECRET_KEY')    # Секретный ключ Django (обязательная переменная)

TIME_ZONE = 'Europe/Moscow'    # Настройки времени

USE_TZ = True
