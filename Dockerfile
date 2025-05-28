FROM python:3.12-alpine AS builder

RUN apk add --no-cache gcc musl-dev linux-headers

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY static/ ./static/
COPY healthcheck.py .

FROM python:3.12-alpine

LABEL org.opencontainers.image.author="Sofiia Laba" \
      org.opencontainers.image.description="Weather App for fetching weather data" \
      org.opencontainers.image.version="1.0"

WORKDIR /app
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
  CMD python /app/healthcheck.py

RUN --mount=type=secret,id=openweather_api_key \
    echo "SECRET's USED"

CMD ["python", "app.py"]