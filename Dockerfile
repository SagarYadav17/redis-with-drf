FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000

RUN python manage.py migrate --no-input

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
