FROM python:3.13.14-alpine

WORKDIR /app

RUN apk add --no-cache git curl bash

RUN pip install --no-cache-dir uv
COPY uv.lock pyproject.toml README.md ./
RUN uv sync --no-dev

COPY . .

ENV PYTHONPATH=/app
EXPOSE 5000

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]