ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install dependencies first for better build caching.
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy application source.
COPY . .

# Run as a fixed non-root UID/GID required by some platforms (e.g., Choreo).
RUN addgroup --gid 10001 appgroup \
    && adduser --disabled-password --gecos "" --uid 10001 --gid 10001 appuser \
    && chown -R 10001:10001 /app
USER 10001

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
