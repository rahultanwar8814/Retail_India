FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
EXPOSE 8080
# CMD ["python", "manage.py", "runserver", ]
