import os
from datetime import datetime

def write_report(domain, data_dict):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reports/{domain.replace('.', '_')}_{timestamp}.txt"

    os.makedirs("reports", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Recon Report for {domain}\n")
        f.write(f"Generated on: {timestamp}\n")
        f.write("=" * 60 + "\n\n")

        for section, content in data_dict.items():
            f.write(f"[{section.upper()}]\n")
            if isinstance(content, dict):
                for key, values in content.items():
                    f.write(f"{key}: {values}\n")
            elif isinstance(content, list):
                for item in content:
                    f.write(f"- {item}\n")
            else:
                f.write(str(content) + "\n")
            f.write("\n")

    print(f"\n✅ Report saved to: {filename}")
