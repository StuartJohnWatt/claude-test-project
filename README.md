# Sales Data Pipeline

A containerised REST API that reads a CSV of sales data and serves summaries and charts over HTTP.

Built with FastAPI, Polars, and Matplotlib. Runs via Docker.

## Requirements

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Setup

1. Add your sales data file at `data/sales.csv`. The file should have the following columns:

   | Column | Type | Example |
   |--------|------|---------|
   | `date` | date | `2024-01-15` |
   | `category` | string | `Electronics` |
   | `units_sold` | integer | `42` |
   | `revenue` | float | `1999.99` |

2. Build and start the API:

   ```bash
   docker compose up --build
   ```

3. The API is available at `http://localhost:8000`.

## Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Health check |
| `GET /summary` | Revenue and units sold grouped by category |
| `GET /monthly` | Revenue grouped by month |
| `GET /chart/category` | Bar chart of revenue by category (PNG) |
| `GET /chart/monthly` | Line chart of monthly revenue trend (PNG) |

Interactive API docs are available at `http://localhost:8000/docs`.

## Stopping the API

```bash
docker compose down
```
