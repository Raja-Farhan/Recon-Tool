import requests
from utils.logger import setup_logger

logger = setup_logger()

def run(domain):
    try:
        url = f"http://{domain}"
        response = requests.get(url, timeout=10)
        headers = response.headers

        techs = []

        server = headers.get('Server')
        if server:
            techs.append(f"Server: {server}")

        x_powered = headers.get('X-Powered-By')
        if x_powered:
            techs.append(f"X-Powered-By: {x_powered}")

        content = response.text.lower()
        if 'wp-content' in content or 'wordpress' in content:
            techs.append("WordPress detected")
        if 'django' in content:
            techs.append("Django detected")
        if 'php' in content:
            techs.append("PHP detected")

        logger.info(f"Technologies detected for {domain}: {techs}")
        return techs
    except Exception as e:
        logger.error(f"Technology detection failed: {e}")
        return {"error": f"Technology detection failed: {e}"}
