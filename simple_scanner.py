import socket
import threading
from datetime import datetime
import sys

# --- הגדרות ורשימת פורטים ---
target = input("Enter Target IP or Hostname: ")
ports_to_scan = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 139: "NetBIOS", 443: "HTTPS",
    445: "SMB", 3306: "MySQL", 3389: "RDP", 8080: "HTTP-Proxy"
}

print("-" * 50)
print(f"[*] SUPER SCANNER v1.0 STARTING ON: {target}")
print(f"[*] TIME STARTED: {datetime.now().strftime('%H:%M:%S')}")
print("-" * 50)

open_ports = []

# פונקציית הסריקה עבור פורט בודד
def scan_port(port, service):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            output = f"[+] PORT {port:5} | OPEN   | SERVICE: {service}"
            print(output)
            open_ports.append(output)
        s.close()
    except:
        pass

# יצירת "חוטים" (Threads) לסריקה מהירה במקביל
threads = []
for port, service in ports_to_scan.items():
    t = threading.Thread(target=scan_port, args=(port, service))
    threads.append(t)
    t.start()

# המתנה לכל ה-Threads שיסיימו
for t in threads:
    t.join()

# --- שמירת התוצאות לקובץ דוח ---
filename = f"scan_report_{target.replace('.', '_')}.txt"
with open(filename, "w") as f:
    f.write(f"CYBER SCAN REPORT\nTarget: {target}\nDate: {datetime.now()}\n")
    f.write("-" * 30 + "\n")
    if open_ports:
        for p in open_ports:
            f.write(p + "\n")
    else:
        f.write("No open ports found.\n")

print("-" * 50)
print(f"[*] SCAN COMPLETE. Found {len(open_ports)} open ports.")
print(f"[*] Report saved as: {filename}")