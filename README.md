# Python Ping Scanner

A Python-based ICMP ping scanner for discovering live hosts on a network.  
This repository contains **two versions**:

1. **Interactive version** – prompts for IP/subnet and ping count.  
2. **CLI version** – fully command-line driven with CSV export.

---

## Features

- Scan a single IP or an entire subnet
- Ping multiple times with concurrency
- Reports alive hosts, total hosts scanned, and scan duration
- Export results to CSV (CLI version)
- Cross-platform (Python 3.8+)

---

## Requirements

- Python 3.8+
- [`icmplib`](https://pypi.org/project/icmplib/) library

Install dependencies:

```bash
pip install icmplib

python ping_scanner.py

Please enter the IP address or subnet: 192.168.1.0/24
Please enter number of times to ping: 2


This addresses are being scanned: 192.168.1.0/24
[Host(address='192.168.1.1'), Host(address='192.168.1.5')]
2 Hosts are up
254 Hosts scanned
This scan took 1.42 seconds

python ping_scanner_cli.py -t 192.168.1.0/24 -c 2 -o results.csv

Scanning 254 hosts...
Scan completed in 1.42 seconds.
2 hosts are up out of 254 scanned.

Alive Hosts:
192.168.1.1
192.168.1.5
Alive hosts saved to 'results.csv'.

