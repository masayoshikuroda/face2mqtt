FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:0.9.2 /uv /usr/local/bin/uv

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libxcb1 \
    && rm -rf /var/lib/apt/lists/*
    
RUN mkdir /opt/face2mqtt
WORKDIR /opt/face2mqtt
COPY pyproject.toml .
COPY uv.lock .
COPY main.py .
COPY facedetector.py .
COPY ipcamera.py .

RUN uv sync --frozen --no-cache

CMD ["uv", "run", "main.py"]