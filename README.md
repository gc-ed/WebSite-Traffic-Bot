# Traffic Bot Project

This project runs a Dockerized traffic simulation bot that visits a target website to increase measurable KPIs.

## Prerequisites
- Docker
- Docker Compose

## Setup
1. Ensure the `.env` file is present and configured with `TARGET_URL` and `PROXY_LIST` (optional).
2. Update `config/targets.json` with the paths you want the bot to visit.
3. In the `.env` file, there is a variable `AUTO_DISCOVER_ROUTES=true`. It crawls the site on every startup and then every 30 days. If it fails to crawl it,  if takes the default variables found in `config/targets.json` folder.

## Build and Run
> **Important:** All Docker commands should be executed from within your Linux Subsystem (WSL Ubuntu), not from Windows PowerShell or Command Prompt.

To build the Docker image:
```bash
docker build -t traffic-bot .
```

To run the bot in the background using Docker Compose:
```bash
docker compose up -d
```

To stop the bot:
```bash
docker compose down
```

## Logs and KPIs
KPI metrics are recorded in `logs/kpi.log` in JSONL format. You can view the logs in real-time by running:
```bash
tail -f logs/kpi.log
```
