FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8282
CMD ["daphne", "-b", "0.0.0.0", "-p", "8282", "project_name.asgi:application"]
