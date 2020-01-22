#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imitation.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


'''
django-admin startproject imitation

создадим виртуальное окружение
python3 -m venv i_api
и запустим его
source i_api/bin/activate

создадим БД по умолчанию
python manage.py migrate

запускаем сервер
python manage.py runserver

установим
pip install djangorestframework

создаем приложение article
python manage.py startapp article

прописываем модели и проводим миграцию:
создаем файлы миграции
python manage.py makemigrations
запуск миграции
python manage.py migrate
посмотреть данные можно в SQLiteStudio

создадим пользователя с правами администратора
python manage.py createsuperuser
imitation/imitation
http://127.0.0.1:8000/admin/login/




'''
