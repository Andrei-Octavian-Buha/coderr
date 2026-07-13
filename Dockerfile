FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalăm dependințe de sistem necesare
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copiem requirements și instalăm (asigură-te că gunicorn este în requirements.txt!)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiem codul
COPY . .

# Colectăm staticele
RUN python manage.py collectstatic --noinput

# Expunem portul
EXPOSE 8000

# Folosim calea completă către gunicorn (poate fi găsită cu 'which gunicorn' în container)
# Dacă pip l-a instalat, ar trebui să fie în /usr/local/bin/gunicorn
CMD ["/usr/local/bin/gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
