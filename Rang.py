import socket
import os
import threading
from tabulate import tabulate
from progress.spinner import Spinner

logo = """
 ____                        ____                  
|  _ \ __ _ _ __   __ _  ___/ ___|  ___ __ _ _ __  
| |_) / _` | '_ \ / _` |/ _ \___ \ / __/ _` | '_ \ 
|  _ < (_| | | | | (_| |  __/___) | (_| (_| | | | |
|_| \_\__,_|_| |_|\__, |\___|____/ \___\__,_|_| |_|
                  |___/                 by Manisso                    
"""

lock = threading.Lock()

def scan_ip(ip, ports, results, progress_bar):
    open_ports = []
    server_info = ""

    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        hostname = "N/A"

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
                if port == 80:
                    sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
                    response = sock.recv(1024).decode()
                    if "Server:" in response:
                        server_info = response.split("Server:")[1].split("\r\n")[0].strip()
            sock.close()
        except socket.error:
            pass

    with lock:
        results.append([ip, hostname, ', '.join(map(str, open_ports)), server_info])
        progress_bar.next()

def scan_ip_range():
    os.system('clear')
    print(logo)
    start_ip = input("Enter the starting IP address: ")
    end_ip = input("Enter the ending IP address: ")

    results = []
    threads = []
    ip_parts = start_ip.split('.')
    start = int(ip_parts[3])
    end = int(end_ip.split('.')[3])

    print("\n[1]- Fast Scan (ports 1 to 1024)")
    print("[2]- Common Port Scan")
    print("[3]- Custom Port Scan (input specific ports separated by commas)")
    print("[0]- EXIT\n")
    scan_type = input("Choose the scan type: ")

    if scan_type == "1":  # Fast Scan (ports 1 to 1024)
        ports = range(1, 1025)
    elif scan_type == "2":  # Common Port Scan
        ports = [
            20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 81, 88, 110, 111, 135, 137,
            138, 139, 143, 161, 162, 443, 445, 465, 514, 587, 631, 636, 993, 995,
            2000, 2049, 3306, 3389, 5432, 5900, 5901, 8080, 8443, 8888, 9000,
            10000, 27017, 28017, 3000, 3300, 4444, 5902, 6660, 6661, 8000, 8081,
            9001, 12345
        ]
    elif scan_type == "0":
        os.system('clear')
        exit()
    elif scan_type == "3":  # Custom Port Scan
        custom_ports = input("Enter the ports to scan (comma-separated): ")
        ports = [int(port) for port in custom_ports.split(",")]
    else:
        print("Invalid scan type. Please choose 1, 2, or 3.")
        return

    progress_bar = Spinner('Scanning..... ')
    for i in range(start, end + 1):
        ip = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{i}"
        thread = threading.Thread(target=scan_ip, args=(ip, ports, results, progress_bar))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    progress_bar.finish()

    headers = ["IP", "Hostname", "OPEN PORT", "Server Info"]
    print(tabulate(results, headers, tablefmt="fancy_grid"))

# Example usage: scan IP range from user input
scan_ip_range()

while True:
    answer = input("\nDo you want to return to the menu? (Yes/No): ")
    if answer.lower() in ["yes", "y", "ya", "ye"]:
      os.system('python main.py')
      break
    elif answer.lower() in ["no", "n", "na", "nn"]:
      os.system('clear')
      exit()