import json
import os
import sys
from datetime import datetime
from loguru import logger
from bot.config import config

logger.remove()
logger.add(sys.stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>")

def log_kpi(session_id: str, pages_visited: int, duration_seconds: int, paths: list, user_agent: str, proxy: str, bounce: bool):
    """Logs KPI data to a JSONL file."""
    log_data = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "session_id": session_id,
        "pages_visited": pages_visited,
        "duration_seconds": duration_seconds,
        "paths": paths,
        "user_agent": user_agent,
        "proxy": proxy,
        "bounce": bounce
    }
    
    log_dir = os.path.dirname(config.kpi_log_path)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)
        
    try:
        with open(config.kpi_log_path, "a") as f:
            f.write(json.dumps(log_data) + "\n")
    except Exception as e:
        logger.error(f"Failed to write to KPI log file: {e}")
