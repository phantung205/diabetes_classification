FROM python:3.10-slim

WORKDIR /phan_tung

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src ./src
COPY app.py ./app.py
COPY templates ./templates
COPY static ./static
COPY routes ./routes
COPY services ./services

EXPOSE 5000

CMD ["python", "app.py"]