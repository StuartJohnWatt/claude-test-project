# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the API

```bash
docker compose up --build   # build and start
docker compose down         # stop and remove containers
```

The API runs at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

The API requires `data/sales.csv` to be present (gitignored). Expected columns: `date`, `category`, `units_sold`, `revenue`.

## Architecture

The app is a single-service FastAPI app containerised with Docker.

- `app/main.py` — route definitions; thin layer that wires pipeline and chart functions to HTTP endpoints
- `app/pipeline.py` — data loading and aggregation using Polars; reads from `/data/sales.csv` inside the container (mounted from `./data/`)
- `app/charts.py` — Matplotlib chart generation; returns PNG bytes directly (no files written to disk)

Charts are generated in memory on every request and streamed as `image/png` responses — there is no caching or file output.
