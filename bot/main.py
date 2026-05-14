import time
import random
from bot.config import config
from bot.logger import logger
from bot.browser import run_session
from bot.crawler import discover_internal_routes

last_scan_time = 0
# Rescan interval in seconds (30 days)
RESCAN_INTERVAL = 30 * 24 * 60 * 60

def refresh_routes_if_needed():
    global last_scan_time
    if config.auto_discover_routes:
        current_time = time.time()
        # Scan if it's the first time OR if 30 days have passed
        if current_time - last_scan_time >= RESCAN_INTERVAL:
            routes = discover_internal_routes(config.target_url)
            if routes:
                config.target_routes = routes
                last_scan_time = current_time
            elif not config.target_routes:
                # If auto-discovery fails and we have no fallback, we must stop
                logger.error("No routes discovered and targets.json is empty. Cannot run traffic.")

def run_all_sessions():
    logger.info(f"Starting traffic generation run: {config.sessions_per_run} sessions.")
    for i in range(config.sessions_per_run):
        try:
            run_session(i)
        except Exception as e:
            logger.error(f"Critical error in session {i}: {e}")
        
        # Slight delay between sessions to avoid instant overlap
        time.sleep(random.uniform(2, 5))

def main():
    while True:
        refresh_routes_if_needed()
        
        if config.target_routes:
            run_all_sessions()
        else:
            logger.warning("Skipping run because no target routes are available.")
            
        logger.info(f"Run complete. Sleeping for {config.run_interval_min} minutes.")
        time.sleep(config.run_interval_min * 60)

if __name__ == "__main__":
    main()
