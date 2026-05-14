import time
import random
import uuid
from typing import Optional
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright
from bot.config import config
from bot.logger import logger, log_kpi

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15"
]

def simulate_scroll(page):
    if not config.scroll_simulation:
        return
    try:
        scrolls = random.randint(2, 5)
        for _ in range(scrolls):
            scroll_amount = random.randint(300, 800)
            page.mouse.wheel(0, scroll_amount)
            time.sleep(random.uniform(1, 3))
    except Exception as e:
        logger.warning(f"Error during scroll simulation: {e}")

def run_session(session_index: int):
    session_id = str(uuid.uuid4())
    logger.info(f"Starting session {session_index + 1}/{config.sessions_per_run} (ID: {session_id})")
    
    user_agent = random.choice(USER_AGENTS) if config.user_agent_rotate else None
    proxy_url = random.choice(config.proxy_list) if config.proxy_list else None
    proxy_settings = {"server": proxy_url} if proxy_url else None

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=user_agent,
            proxy=proxy_settings,
            viewport={'width': random.randint(1024, 1920), 'height': random.randint(768, 1080)}
        )
        page = context.new_page()

        visited_paths = []
        session_start_time = time.time()
        
        try:
            pages_to_visit = min(config.pages_per_session, len(config.target_routes))
            routes_to_visit = random.sample(config.target_routes, pages_to_visit)
            
            for i, route in enumerate(routes_to_visit):
                url = urljoin(config.target_url, route)
                logger.info(f"Visiting ({i+1}/{pages_to_visit}): {url}")
                page.goto(url, wait_until="domcontentloaded", timeout=30000)
                visited_paths.append(route)
                
                # Simulate human behavior
                simulate_scroll(page)
                
                # Wait for dwell time
                dwell_time = random.uniform(config.dwell_time_min, config.dwell_time_max)
                time.sleep(dwell_time)
                
        except Exception as e:
            logger.error(f"Session {session_id} encountered an error: {e}")
        finally:
            session_duration = int(time.time() - session_start_time)
            bounce = len(visited_paths) < 2
            log_kpi(session_id, len(visited_paths), session_duration, visited_paths, user_agent, proxy_url, bounce)
            logger.info(f"Session {session_id} finished in {session_duration}s. Pages visited: {len(visited_paths)}")
            browser.close()
