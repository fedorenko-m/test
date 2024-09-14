# Используем Python как базовый образ
FROM python:3.8-slim

# Устанавливаем рабочую директорию
WORKDIR /https

# Копируем файлы в контейнер
COPY . /https

# Устанавливаем зависимости
RUN pip install flask

# Запуск приложения
CMD ["python", "https_endpoint.py"]
