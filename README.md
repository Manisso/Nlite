![alt logo](https://i.ibb.co/4W3SmhY/image-2024-05-07-191410351.png)

# N-lite IP Scanner Tool
## Overview
N-lite is a versatile IP scanner tool designed for network administrators and security professionals. It provides comprehensive scanning capabilities for both single IP addresses and IP ranges. With N-lite, users can scan for open ports, retrieve protocol information from banners, and gather detailed server information. The tool offers a user-friendly interface and supports customizable scan options to suit different scanning needs.

## IP Range Scan Menu
When scanning IP ranges, N-lite offers the following menu:

- Enter the starting IP address: [User Input]
- Enter the ending IP address: [User Input]

### Scan Options:
+ [1] Fast Scan (ports 1 to 1024)
+ [2] Common Port Scan
+ [3] Custom Port Scan (input specific ports separated by commas)

![alt logo](https://i.ibb.co/gS5T8SM/Capture-d-cran-2024-05-07-050014.png)

## IP Port Scan Menu
For scanning single IP addresses, N-lite provides the following menu:

### Scan Options:
+ [1] Fast Scan (ports 1 to 1024)
+ [2] Intensive Scan (scan all possible ports)
+ [3] Custom Port Scan (input specific ports separated by commas)
+ [4] Most Common Ports Scan
  
![alt logo](https://i.ibb.co/9gpNRpH/Capture-d-cran-2024-05-07-045704.png)

## Features
* Port Scanning: Scan for open ports on single IP addresses or IP ranges.
* Banner Grabbing: Retrieve protocol information from banners of open ports.
* Server Information: Gather detailed server information, including server type, and application versions.
* Cross-Platform Support: Compatible with Windows, macOS, and Linux.

## How to Install
```bash
bash <(wget -qO- https://t.ly/NgFUV)
```
To create a symbolic link named python that points to python3 in the /usr/bin directory, you can use the following command:

```bash
sudo ln -s /usr/bin/python3 /usr/bin/python
```

This command creates a symbolic link called python in /usr/bin that points to the python3 executable. This way, when you use the python command, it will effectively run Python 3.
