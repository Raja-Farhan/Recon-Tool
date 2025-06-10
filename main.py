import argparse

from modules.whois_lookup import run as perform_whois
from modules.dns_enum import run as dns_lookup
from modules.subdomain_enum import run as get_subdomains
from modules.port_scanner import run as scan_ports
from modules.banner_grabber import run as grab_banners
from modules.tech_detect import run as detect_technologies

from utils.report_writer import write_report

def main():
    parser = argparse.ArgumentParser(description="Custom Reconnaissance Tool")
    parser.add_argument("domain", help="Target domain (e.g., example.com)")
    parser.add_argument("--whois", action="store_true", help="Perform WHOIS lookup")
    parser.add_argument("--dns", action="store_true", help="Perform DNS enumeration")
    parser.add_argument("--subdomain", action="store_true", help="Enumerate subdomains")
    parser.add_argument("--portscan", action="store_true", help="Scan ports")
    parser.add_argument("--banners", action="store_true", help="Grab service banners")
    parser.add_argument("--tech", action="store_true", help="Detect technologies used")

    args = parser.parse_args()
    domain = args.domain
    report_data = {}

    if args.whois:
        print("\n[+] WHOIS Lookup")
        result = perform_whois(domain)
        print(result)
        report_data["whois"] = result

    if args.dns:
        print("\n[+] DNS Enumeration")
        result = dns_lookup(domain)
        print(result)
        report_data["dns"] = result

    if args.subdomain:
        print("\n[+] Subdomain Enumeration")
        result = get_subdomains(domain)
        print(result)
        report_data["subdomains"] = result

    if args.portscan:
        print("\n[+] Port Scanning")
        result = scan_ports(domain)
        print(result)
        report_data["ports"] = result

    if args.banners:
        print("\n[+] Banner Grabbing")
        result = grab_banners(domain)
        print(result)
        report_data["banners"] = result

    if args.tech:
        print("\n[+] Technology Detection")
        result = detect_technologies(domain)
        print(result)
        report_data["technologies"] = result

    if report_data:
        write_report(domain, report_data)

if __name__ == "__main__":
    main()
