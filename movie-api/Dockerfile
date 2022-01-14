FROM python:latest

WORKDIR /app

COPY . .

RUN apt-get update
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]