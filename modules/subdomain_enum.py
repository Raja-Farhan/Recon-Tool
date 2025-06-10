import requests
from utils.logger import setup_logger

logger = setup_logger()

def run(domain):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        subdomains = set()
        for entry in data:
            name = entry.get('name_value')
            if name:
                for sub in name.split('\n'):
                    if sub.endswith(domain):
                        subdomains.add(sub.strip())
        logger.info(f"Found {len(subdomains)} subdomains for {domain}")
        return list(subdomains)
    except Exception as e:
        logger.error(f"Subdomain enumeration failed: {e}")
        return {"error": f"Subdomain enumeration failed: {e}"}
