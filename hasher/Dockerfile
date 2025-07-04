FROM python:3.12-slim
WORKDIR /app
COPY hasher.py .
RUN pip install bcrypt
CMD ["python", "hasher.py"]
