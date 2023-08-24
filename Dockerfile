FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Создание виртуального окружения
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Копирование файлов и установка зависимостей
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py migrate

# Запуск Gunicorn приложения
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]