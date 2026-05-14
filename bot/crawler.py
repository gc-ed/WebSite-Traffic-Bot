import urllib.request
from urllib.parse import urljoin, urlparse
from html.parser import HTMLParser
from bot.logger import logger

class LinkExtractor(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.base_netloc = urlparse(base_url).netloc
        self.internal_routes = set(['/'])

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href':
                    # Skip anchor links or javascript
                    if value.startswith('#') or value.startswith('javascript:'):
                        continue
                    
                    full_url = urljoin(self.base_url, value)
                    parsed = urlparse(full_url)
                    
                    # Check if the link points to the same domain and is HTTP/HTTPS
                    if parsed.netloc == self.base_netloc and parsed.scheme in ('http', 'https'):
                        path = parsed.path
                        if not path:
                            path = '/'
                        # Keep query params if any, otherwise just path
                        if parsed.query:
                            path = f"{path}?{parsed.query}"
                        self.internal_routes.add(path)

def discover_internal_routes(target_url: str) -> list:
    """Fetches the target URL homepage and extracts internal routing paths."""
    logger.info(f"Auto-Discovery: Scanning {target_url} for internal links...")
    
    try:
        # Define a standard User-Agent so we don't get blocked
        req = urllib.request.Request(
            target_url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            html_content = response.read().decode('utf-8', errors='ignore')
            
        parser = LinkExtractor(target_url)
        parser.feed(html_content)
        
        routes = list(parser.internal_routes)
        logger.info(f"Auto-Discovery complete. Found {len(routes)} internal routes.")
        return routes
        
    except Exception as e:
        logger.error(f"Auto-Discovery failed: {e}")
        return []
