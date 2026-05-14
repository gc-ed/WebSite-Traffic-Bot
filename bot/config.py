import os
import json
from dataclasses import dataclass
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    target_url: str
    sessions_per_run: int
    pages_per_session: int
    dwell_time_min: int
    dwell_time_max: int
    scroll_simulation: bool
    user_agent_rotate: bool
    proxy_list: List[str]
    kpi_log_path: str
    run_interval_min: int
    target_routes: List[str]
    auto_discover_routes: bool

def load_config() -> Config:
    target_url = os.getenv("TARGET_URL")
    if not target_url:
        raise ValueError("TARGET_URL is required in .env")

    # Parse proxies
    proxy_env = os.getenv("PROXY_LIST", "")
    proxy_list = [p.strip() for p in proxy_env.split(",") if p.strip()]

    # Load targets.json
    targets_path = os.path.join(os.path.dirname(__file__), "..", "config", "targets.json")
    try:
        with open(targets_path, "r") as f:
            targets_data = json.load(f)
            routes = targets_data.get("routes", ["/"])
    except FileNotFoundError:
        routes = ["/"]
        
    return Config(
        target_url=target_url,
        sessions_per_run=int(os.getenv("SESSIONS_PER_RUN", "10")),
        pages_per_session=int(os.getenv("PAGES_PER_SESSION", "4")),
        dwell_time_min=int(os.getenv("DWELL_TIME_MIN", "15")),
        dwell_time_max=int(os.getenv("DWELL_TIME_MAX", "60")),
        scroll_simulation=os.getenv("SCROLL_SIMULATION", "true").lower() == "true",
        user_agent_rotate=os.getenv("USER_AGENT_ROTATE", "true").lower() == "true",
        proxy_list=proxy_list,
        kpi_log_path=os.getenv("KPI_LOG_PATH", "/logs/kpi.log"),
        run_interval_min=int(os.getenv("RUN_INTERVAL_MIN", "30")),
        target_routes=routes,
        auto_discover_routes=os.getenv("AUTO_DISCOVER_ROUTES", "false").lower() == "true"
    )

config = load_config()
