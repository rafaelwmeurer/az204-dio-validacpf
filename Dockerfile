FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 7071
CMD ["python", "-m", "uvicorn", "function_app:app", "--host", "0.0.0.0", "--port", "7071"]