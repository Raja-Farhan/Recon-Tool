# 🕵️ Recon Tool - Modular Reconnaissance CLI Tool

A lightweight and modular reconnaissance tool built in Python to automate initial information gathering during penetration testing and red team engagements.

## 🚀 Features

🔹 **Passive Recon:**
- WHOIS Lookup
- DNS Enumeration (A, MX, TXT, NS)
- Subdomain Enumeration (using crt.sh, AlienVault, etc.)

🔹 **Active Recon:**
- Port Scanning (via `python-nmap`)
- Banner Grabbing
- Technology Detection (e.g., via headers)

🔹 **Reporting:**
- Generates `.txt` or `.html` report with timestamps and resolved IPs

🔹 **Modular CLI Interface:**
- Call specific modules using flags (e.g., `--whois`, `--dns`)

---

## 🧪 Sample Usage

```bash
python main.py example.com --whois --dns --subdomain --portscan --banners --tech
