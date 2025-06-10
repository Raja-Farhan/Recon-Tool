import socket
from utils.logger import setup_logger

logger = setup_logger()

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

def run(domain):
    open_ports = []
    try:
        ip = socket.gethostbyname(domain)
        logger.info(f"Starting port scan on {domain} ({ip})")
        for port in COMMON_PORTS:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            sock.close()
            if result == 0:
                open_ports.append(port)
        logger.info(f"Open ports found: {open_ports}")
        return {"ip": ip, "open_ports": open_ports}
    except Exception as e:
        logger.error(f"Port scanning failed: {e}")
        return {"error": f"Port scanning failed: {e}"}
