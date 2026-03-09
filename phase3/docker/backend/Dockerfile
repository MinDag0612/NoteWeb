FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY backendSrc/requirements.txt /app/backendSrc/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/backendSrc/requirements.txt

COPY backendSrc /app/backendSrc

RUN addgroup --system app && adduser --system --ingroup app app \
    && mkdir -p /app/uploads \
    && chown -R app:app /app

USER app

EXPOSE 8000

CMD ["gunicorn", "backendSrc.main:app", "--bind", "0.0.0.0:8000", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker"]
