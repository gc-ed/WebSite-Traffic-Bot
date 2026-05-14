# memory.md — Agent Persistent Memory

> **Agent rule:** This file is your long-term memory. Read it at the start of EVERY session. Append a new entry at the end of EVERY session. Never delete past entries. If this file is empty or missing, that means this is Session 1 — initialize it now.

---

## 🧭 How to Use This File

- **On session start:** Read ALL entries below. Reconstruct your understanding of project state.
- **On session end:** Append a new `## Session [N]` block (see format below).
- **On task completion:** Note it here AND update `TASKS.md`.
- **On discovery:** If you find something unexpected (a bug, a missing file, a config issue), log it here immediately.

---

## 📋 Project State Summary

> *Agent: Keep this section updated. Rewrite it each session to reflect current reality.*

| Field                  | Value                                  |
|------------------------|----------------------------------------|
| Project name           | Traffic Bot                            |
| Current phase          | 🟢 Operations — bot is actively running |
| Last active session    | Session 1                              |
| Docker status          | ✅ Built and Running                    |
| Bot status             | ✅ Implemented                         |
| Target URL             | ✅ Configured (https://www.ng-soc.eu/) |
| Last traffic run       | 2026-05-14 (Session 1)                 |
| KPI status             | 🟢 Logging data successfully           |
| Blockers               | None                                   |

---

## 📊 KPI Snapshot

> *Agent: Update after every traffic run.*

| KPI                    | Target     | Last Measured | Status  |
|------------------------|------------|---------------|---------|
| Sessions / day         | ≥ 100      | —             | ⚠️ N/A  |
| Pages / session        | ≥ 3        | —             | ⚠️ N/A  |
| Avg. session duration  | ≥ 45s      | —             | ⚠️ N/A  |
| Bounce rate            | ≤ 30%      | —             | ⚠️ N/A  |
| Route coverage         | ≥ 80%      | —             | ⚠️ N/A  |

---

## 🗒️ Session Log

---

### Session 1 — 2026-05-14T10:00:00Z

**What I did this session:**
- [x] Read `AGENTS.md`
- [x] Read `TASKS.md`
- [x] Read `memory.md`
- [x] Created `.env` and `config/targets.json`
- [x] Created bot codebase (`bot/config.py`, `bot/logger.py`, `bot/browser.py`, `bot/main.py`)
- [x] Created `Dockerfile`, `docker-compose.yml`, and `README.md`

**Tasks completed:**
- TASK-001 through TASK-014 (All tasks complete!)

**Tasks moved to IN PROGRESS:**
- (none)

**Tasks blocked:**
- (none)

**Discoveries / notes:**
- Set up target URLs and proxy rotation logic (TASK-013 included in browser logic).
- Transitioned to loguru for logging.
- Fixed Docker build dependencies by switching to official mcr.microsoft.com/playwright image.
- Tested and verified container is correctly running and simulating traffic via WSL.

**Files created/modified this session:**
- `.env`, `config/targets.json`, `.gitignore`
- `bot/config.py`, `bot/logger.py`, `bot/browser.py`, `bot/main.py`
- `Dockerfile`, `docker-compose.yml`, `requirements.txt`, `README.md`
- `TASKS.md`, `memory.md`

**Next session should start with:**
- Monitoring KPIs (Sessions/day, Bounce rate) and making any requested config changes.

---

<!-- AGENT: Add new session blocks below this line. Copy the template above. -->

---

## 🔧 Decisions Log

> *Agent: When you make an architectural or configuration decision, record it here so future sessions understand why.*

| Date | Decision | Reason |
|------|----------|--------|
| *(session 1)* | Used Playwright over Selenium | Better headless Chrome support, async-native, easier scroll simulation |
| *(session 1)* | Used `python:3.11-slim` as base image | Small image size, good Playwright support |
| *(session 1)* | KPI log format: JSON lines (`.jsonl`) | Easier to parse programmatically than plain text |

---

## ⚠️ Known Issues

> *Agent: Log bugs, gaps, or concerns here. Mark resolved ones with ✅.*

| ID     | Issue                          | Status      | Session Found |
|--------|-------------------------------|-------------|---------------|
| *(none yet)* | —                        | —           | —             |

---

## 📦 Dependencies Reference

> *Agent: Keep this updated as you install things.*

| Package          | Version   | Purpose                          |
|------------------|-----------|----------------------------------|
| `playwright`     | latest    | Browser automation               |
| `python-dotenv`  | latest    | Load `.env` into environment     |
| `httpx`          | latest    | Optional: lightweight HTTP calls |
| `loguru`         | latest    | Structured logging               |

---

*This file is maintained automatically by the AI agent. Do not manually edit past sessions.*
