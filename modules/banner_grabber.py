import socket
from utils.logger import setup_logger

logger = setup_logger()

COMMON_PORTS = [80, 443, 21, 22, 25]

def run(domain):
    banners = {}
    try:
        ip = socket.gethostbyname(domain)
        logger.info(f"Starting banner grabbing on {domain} ({ip})")
        for port in COMMON_PORTS:
            try:
                sock = socket.socket()
                sock.settimeout(2)
                sock.connect((ip, port))
                sock.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = sock.recv(1024).decode(errors='ignore').strip()
                banners[port] = banner
                sock.close()
            except Exception as e:
                logger.warning(f"Could not grab banner on port {port}: {e}")
        logger.info(f"Banners grabbed: {list(banners.keys())}")
        return banners
    except Exception as e:
        logger.error(f"Banner grabbing failed: {e}")
        return {"error": f"Banner grabbing failed: {e}"}
