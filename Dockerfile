FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirments.txt

EXPOSE 80

CMD ["fastapi", "run", "app/main.py", "--port", "80"]