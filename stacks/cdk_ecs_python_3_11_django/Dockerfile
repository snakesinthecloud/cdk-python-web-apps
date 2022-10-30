FROM --platform=linux/amd64 python:3.11.0-slim-bullseye

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY manage.py .
COPY db.sqlite3 .
COPY mycdkdjangoapp ./mycdkdjangoapp
COPY polls ./polls

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]