FROM python:3.12-slim
WORKDIR /app
COPY main.py .
RUN pip install fastapi uvicorn requests
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
