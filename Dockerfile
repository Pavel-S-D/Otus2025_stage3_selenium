FROM python:3.14-slim

RUN pip install --no-cache-dir pytest selenium

WORKDIR /app

COPY conftest.py .
COPY tests/ ./tests/

ENTRYPOINT ["pytest"]
