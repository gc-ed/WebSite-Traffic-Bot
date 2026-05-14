# TASKS.md — Agent Task Tracker

> **Agent rule:** Always read this file at session start. Pick the first `TODO` task. Update status as you work. Never leave a task in `IN PROGRESS` at session end — either complete it or mark it `BLOCKED`.

---

---

## 🟡 IN PROGRESS

*(Agent: move tasks here when you start working on them)*

---

## 🟢 DONE

- [x] **TASK-009** — Test Docker build locally
- [x] **TASK-010** — Run first live traffic test
- [x] **TASK-011** — Tune KPI parameters to hit targets (Defaults set to 480 daily sessions)
- [x] **TASK-012** — Set up automated scheduling (Loop-with-sleep implemented in main.py)
- [x] **TASK-001** — Create `.env` file with all required environment variables  
- [x] **TASK-002** — Create `config/targets.json` with full list of page routes to visit  
- [x] **TASK-003** — Write `bot/config.py` — reads and validates all env vars  
- [x] **TASK-004** — Write `bot/browser.py` — browser/session simulation module  
- [x] **TASK-005** — Write `bot/logger.py` — KPI logging module  
- [x] **TASK-006** — Write `bot/main.py` — entry point  
- [x] **TASK-007** — Write `Dockerfile`  
- [x] **TASK-008** — Write `docker-compose.yml`  
- [x] **TASK-013** — Add proxy rotation support  
- [x] **TASK-014** — Write `README.md` — human-readable setup guide  

---

## 🔵 BLOCKED

*(Agent: move tasks here if blocked. Explain the blocker clearly.)*

---

## 📝 Notes for Agent

- Tasks are roughly ordered by dependency — do them top to bottom unless blocked.
- If you discover a new task while working, add it to `TODO` with a `TASK-NNN` ID.
- Never delete tasks — only move them between sections.
- After each session, the `DONE` section should grow.

---

*Last updated by: Agent Session 1*
