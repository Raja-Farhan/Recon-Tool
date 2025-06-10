import whois
from utils.logger import setup_logger

logger = setup_logger()

def run(domain):
    try:
        info = whois.whois(domain)
        logger.info(f"WHOIS lookup successful for {domain}")

        return {key: str(value) for key, value in info.items()}
    except Exception as e:
        logger.error(f"WHOIS lookup failed: {e}")
        return {"error": f"WHOIS lookup failed: {e}"}
