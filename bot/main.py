import time
import random
from bot.config import config
from bot.logger import logger
from bot.browser import run_session

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
        run_all_sessions()
        logger.info(f"Run complete. Sleeping for {config.run_interval_min} minutes.")
        time.sleep(config.run_interval_min * 60)

if __name__ == "__main__":
    main()
