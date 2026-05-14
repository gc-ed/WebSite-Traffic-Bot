# AGENTS.md — Traffic Bot Project

> **For AI Agents (Gemini / antigravity):** This file is your primary instruction set. Read it fully before taking any action. Never lose context of this file — always re-read it at the start of each session.

---

## 📌 Project Overview

This project runs a **Dockerized traffic simulation bot** that visits a target website to increase measurable KPIs (sessions, page views, time on page). It is designed to be:

- Configurable via environment variables
- Repeatable and schedulable (cron / CI)
- KPI-aware (tracks and logs what matters)
- Maintainable by an AI agent without human intervention between runs

---

## 🗂️ Repository Structure

```
/ (root)
├── AGENTS.md              ← YOU ARE HERE — primary agent instructions
├── TASKS.md               ← Task list (to-do, in-progress, done)
├── memory.md              ← Persistent memory log (auto-updated by agent)
├── Dockerfile             ← Docker image definition
├── docker-compose.yml     ← Orchestration (volumes, env, restart policy)
├── bot/
│   ├── main.py            ← Entry point for the traffic bot
│   ├── browser.py         ← Browser/session simulation logic
│   ├── config.py          ← Reads env vars and config
│   └── logger.py          ← KPI logging utilities
├── config/
│   └── targets.json       ← List of URLs and page routes to visit
├── logs/
│   └── kpi.log            ← Output log (mounted as Docker volume)
└── .env                   ← Environment variables (NOT committed to git)
```

---

## 🎯 Target Website

```
TARGET_URL=https://YOUR_WEBSITE_HERE.com
```

> **Agent instruction:** If `TARGET_URL` is not set in `.env`, stop and log a warning to `memory.md`. Do not proceed with broken config.

---

## ⚙️ Environment Variables (`.env`)

| Variable             | Description                                      | Default         |
|----------------------|--------------------------------------------------|-----------------|
| `TARGET_URL`         | Base URL of the website to visit                 | *(required)*    |
| `SESSIONS_PER_RUN`   | Number of simulated sessions per execution       | `10`            |
| `PAGES_PER_SESSION`  | Number of pages visited per session              | `4`             |
| `DWELL_TIME_MIN`     | Minimum time (seconds) spent on each page        | `15`            |
| `DWELL_TIME_MAX`     | Maximum time (seconds) spent on each page        | `60`            |
| `SCROLL_SIMULATION`  | Enable scroll behavior simulation (`true/false`) | `true`          |
| `USER_AGENT_ROTATE`  | Rotate user agents between sessions (`true/false`)| `true`         |
| `PROXY_LIST`         | Comma-separated list of proxy IPs (optional)     | *(empty)*       |
| `KPI_LOG_PATH`       | Path inside container to write KPI logs          | `/logs/kpi.log` |
| `RUN_INTERVAL_MIN`   | Minutes between auto-runs (if looping)           | `30`            |

---

## 📊 KPI Targets

These are the metrics this bot is designed to influence. Log all of these per run:

| KPI                     | Target               | Notes                                      |
|-------------------------|----------------------|--------------------------------------------|
| Sessions / day          | ≥ 100                | Each bot execution = N sessions            |
| Avg. pages per session  | ≥ 3                  | Controlled by `PAGES_PER_SESSION`          |
| Avg. session duration   | ≥ 45 seconds         | Controlled by `DWELL_TIME_MIN/MAX`         |
| Bounce rate             | ≤ 30%                | At least 2 pages visited = not a bounce    |
| Unique paths visited    | Cover ≥ 80% of routes| Defined in `config/targets.json`           |

---

## 🧠 Agent Responsibilities

When operating as an AI agent on this project, you must:

1. **Always read `memory.md` first** — it contains the latest state of the project.
2. **Always read `TASKS.md`** — pick up the next `TODO` task.
3. **After completing any task**, update both `TASKS.md` and `memory.md`.
4. **Never skip the logging step** — every action must be recorded.
5. **If a task is blocked**, mark it `BLOCKED` in `TASKS.md` and explain why in `memory.md`.
6. **Do not modify this file (`AGENTS.md`)** unless explicitly instructed by a human.

---

## 🐳 Docker Instructions

### Build
```bash
docker build -t traffic-bot .
```

### Run (single execution)
```bash
docker run --env-file .env -v $(pwd)/logs:/logs traffic-bot
```

### Run with Compose (looping / scheduled)
```bash
docker-compose up -d
```

### Stop
```bash
docker-compose down
```

---

## 🔒 Safety & Ethics Notes

- This bot is intended for **internal analytics testing** and **owned properties only**.
- Do NOT use against third-party websites without explicit permission.
- Ensure the target site's `robots.txt` and ToS allow automated access.
- Use proxy rotation and rate limiting to avoid overloading the server.
- All traffic should mimic realistic human behavior (dwell time, scrolling, navigation paths).

---

## 🔄 Update Protocol

When the agent completes any work:
1. Append a timestamped entry to `memory.md`
2. Move completed items in `TASKS.md` from `TODO` → `DONE`
3. Add any newly discovered tasks to `TASKS.md` under `TODO`

---

*Last updated by: [AGENT — update this field on each session]*  
*File version: 1.0.0*
