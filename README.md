# 🛡️ Recon Tool

A lightweight, modular reconnaissance tool built in Python for automating initial information gathering in penetration testing and red team engagements.

---

## ✨ Features

- WHOIS Lookup  
- DNS Enumeration (A, MX, TXT, NS Records)  
- Subdomain Enumeration (via external APIs)  
- Port Scanning  
- Banner Grabbing  
- Technology Detection  
- Report Generation (.txt and .html)  
- Logging with Verbosity Levels  
- Modular CLI Flags  
- Docker Support for Containerized Use  

---

## 🛠️ Getting Started

You can use this tool either **natively with Python** or via a **Docker container**.

---

### 🔧 Option 1: Native Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/recon-tool.git
cd recon-tool
```

#### 2. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Run the Tool
```bash
python main.py example.com --whois --dns --subdomain --portscan --banners --tech
```

### 🐳 Option 2: Using Docker

#### 1. Build Docker Image
```bash
docker build -t recon-tool:latest .
```
#### 2. Run the Tool via Docker
```bash
docker run --rm recon-tool:latest example.com --whois --dns --portscan
```
ℹ️ Docker containers are ephemeral. Mount volumes if you want persistent logs or reports.

#### 📂 Output
📝 Reports are saved in the reports/ folder.
📜 Logs are stored in the logs/ folder with timestamps.

#### 🧾 Sample Usage
```bash
python main.py example.com --whois --dns
```

You can use any combination of supported flags:
--whois
--dns
--subdomain
--portscan
--banners
--tech

#### 🗃️ Directory Structure
recon-tool/
├── modules/
│   ├── whois_lookup.py
│   ├── dns_enum.py
│   ├── subdomain_enum.py
│   ├── port_scanner.py
│   ├── banner_grabber.py
│   └── tech_detect.py
├── reports/
├── utils/
│   └── logger.py
├── logs/
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md

#### 📄 License
This project is licensed under the MIT License.

#### 🙌 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss what you'd like to change.
