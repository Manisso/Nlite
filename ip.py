import os
import socket
import http.client
from tabulate import tabulate
from tqdm import tqdm


logo = """
 ____            _   ____                  
|  _ \ ___  _ __| |_/ ___|  by Manisso.__  
| |_) / _ \| '__| __\___ \ / __/ _` | '_ \ 
|  __/ (_) | |  | |_ ___) | (_| (_| | | | |
|_|   \___/|_|   \__|____/ \___\__,_|_| |_|
"""

def scan_ports(target_host, port_range):
  results = []

  with tqdm(total=len(port_range), desc="Scanning Ports") as pbar:
    for port in port_range:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.settimeout(1)

      result = sock.connect_ex((target_host, port))

      if result == 0:
        protocol = get_protocol_name(port)

        if protocol in ["HTTP", "Node.js Debug"]:
          server_info = detect_server_info(target_host, port)
          results.append([port, protocol, server_info])
        elif protocol == "HTTPS":
          server_info = detect_server_info(target_host, port, https=True)
          if server_info == "N/A":
            results.append([port, protocol, server_info])
          else:
            banner_info = detect_banner(target_host, port)
            results.append([port, protocol, banner_info])
        else:
          banner_info = detect_banner(target_host, port)
          results.append([port, protocol, banner_info])

      sock.close()
      pbar.update(1)

  if results:
    print(
        tabulate(results,
                 headers=["Port", "Protocol", "Information"],
                 tablefmt="fancy_grid"))


def get_protocol_name(port):
  protocol_mapping = {
      20: "FTP",
      21: "FTP",
      22: "SSH",
      23: "Telnet",
      25: "SMTP",
      53: "DNS",
      67: "DHCP",
      68: "DHCP",
      69: "TFTP",
      80: "HTTP",
      81: "HTTP",
      88: "Kerberos",
      110: "POP3",
      111: "RPC",
      135: "RPC",
      137: "NetBIOS Name Service",
      138: "NetBIOS Datagram Service",
      139: "NetBIOS Session Service",
      143: "IMAP",
      161: "SNMP",
      162: "SNMP Trap",
      443: "HTTPS",
      445: "SMB",
      465: "SMTP (SSL)",
      514: "Syslog",
      587: "SMTP",
      631: "IPP",
      636: "LDAP (SSL)",
      993: "IMAP (SSL)",
      995: "POP3 (SSL)",
      1433: "Microsoft SQL Server",
      1521: "Oracle Database",
      3306: "MySQL",
      3389: "RDP",
      5432: "PostgreSQL",
      5900: "VNC",
      5901: "VNC",
      8080: "HTTP",
      8443: "HTTPS",
      8888: "HTTP",
      9000: "HTTP",
      10000: "Webmin",
      27017: "MongoDB",
      28017: "MongoDB (HTTP)",
      3000: "Node.js",
      3300: "Node.js",
      4444: "Node.js Debug",
      5902: "VNC",
      6660: "IRC",
      6661: "IRC",
      8000: "HTTP",
      8081: "HTTP",
      9001: "HTTP",
      12345: "NetBus"
      # Add more protocol mappings as needed
  }
  return protocol_mapping.get(port, "Unknown")


def detect_banner(target_host, port):
  try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(1)
    client_socket.connect((target_host, port))
    banner = client_socket.recv(1024)
    client_socket.close()

    try:
      banner = banner.decode('utf-8').strip()
    except UnicodeDecodeError:
      banner = "N/A"

    return banner
  except (socket.timeout, ConnectionRefusedError):
    return "N/A"


def detect_server_info(target_host, port, https=False):
    protocol = "https" if https else "http"
    try:
        conn = http.client.HTTPConnection(target_host, port, timeout=1)
        conn.request("GET", "/")
        response = conn.getresponse()
        server_info = response.getheader("Server")
        if server_info is None:
            server_info = "N/A"
        conn.close()
        return server_info
    except (http.client.HTTPException, socket.timeout, ConnectionResetError):
        return "N/A"


if __name__ == "__main__":
  os.system('clear')
  print(logo)
  target_host = input("\nEnter the Host to scan: ")
  os.system('clear')
  target_ip = socket.gethostbyname(
      target_host)  # Get the IP address of the target host
  print (logo)
  print(f"Scanning host: {target_ip}\n")

  print(" Choose a port scanning type:\n")
  print("[1]- Fast Scan (ports 1 to 1024)")
  print("[2]- Intensive Scan (scan all possible ports)")
  print("[3]- Custom Port Scan (input specific ports separated by commas)")
  print("[4]- Most Common Ports Scan <-")
  print("[0]- EXIT")

  scan_type = input("\n>>> ")

  if scan_type == "1":
    port_range = range(1, 1025)
  elif scan_type == "2":
    port_range = range(1, 65536)
  elif scan_type == "3":
    custom_ports = input("Enter the ports to scan (comma-separated): ")
    port_range = [int(port) for port in custom_ports.split(",")]
  elif scan_type == "4":
    port_range = [
        20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 81, 88, 110, 111, 135, 137,
        138, 139, 143, 161, 162, 443, 445, 465, 514, 587, 631, 636, 993, 995,
        2000, 2049, 3306, 3389, 5432, 5900, 5901, 8080, 8443, 8888, 9000,
        10000, 27017, 28017, 3000, 3300, 4444, 5902, 6660, 6661, 8000, 8081,
        9001, 12345
    ]
  elif scan_type == "0":
    exit()
  else:
    print("Invalid scan type. Please choose 1, 2, 3, 4, or 0.")
    exit()
  scan_ports(target_ip, port_range)
while True:
    answer = input("\nDo you want to return to the menu? (Yes/No): ")
    if answer.lower() in ["yes", "y", "ya", "ye"]:
      os.system('python main.py')
      break
    elif answer.lower() in ["no", "n", "na"]:
      os.system('clear')
      exit()
    else:
      print("Invalid input. Please enter Yes/No.")