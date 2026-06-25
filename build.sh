#!/usr/bin/env bash


echo "Устанавливаем зависимости..."
pip install -r requirements.txt

echo "Собираем статику..."
python manage.py collectstatic --noinput

echo "Выполняем миграции..."
python manage.py migrate

echo "Запускаем приложение..."
gunicorn news_portal2.wsgi:application --log-file -