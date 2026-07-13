# syntax=docker/dockerfile:1
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


COPY . . 
# (restul liniilor de dinainte)

# 9. Comanda pentru pornirea aplicației cu Gunicorn
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
