FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .

# VULNERABILITY 4: Running as root user (Trivy scanner will hate this)
RUN pip install --no-cache-dir -r requirements.txt


# docker run -p 5001:5000 golden-app - using 5001 for laptop as 5000 is busy.
EXPOSE 5000

CMD ["python", "app.py"]