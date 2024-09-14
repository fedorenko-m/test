# Используем Python как базовый образ
FROM python:3.8-slim

# Устанавливаем рабочую директорию
WORKDIR /scheduler

# Копируем файлы в контейнер
COPY . /scheduler

# Устанавливаем зависимости
RUN pip install flask

# Запуск приложения
CMD ["python", "scheduler_endpoint.py"]
