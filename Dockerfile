# Используем образ Python
FROM python:3.8

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Копируем приложение
COPY . .

# Запускаем приложение
CMD ["python", "app.py"]
