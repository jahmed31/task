FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# updating to container and adding other packages to run services smoothly
RUN apt-get update && apt-get install -y netcat-traditional && apt-get clean
RUN pip install --upgrade pip

# working directory to be as code
WORKDIR /code

# copying requirement file and running it to install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY ./smart /code

# this batch command wait for database container to run so later
# migrations and collectstatic can be collected
COPY wait_for_db.sh /wait_for_db.sh
RUN chmod +x /wait_for_db.sh

# Run server with gunicorn
CMD ["gunicorn", "smart.wsgi:application", "w", "6", "--bind", "0.0.0.0:8000"]