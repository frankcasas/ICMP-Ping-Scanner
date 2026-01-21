# ICMP-Ping-Scanner
ICMP Ping Scanner


A simple Python-based ping scanner that discovers active hosts on a given IP address or subnet by sending ICMP echo requests using the icmplib library.

This tool prompts the user for a target IP or subnet and the number of ping attempts, then reports how many hosts are alive and how long the scan took.

Features

Scan a single IP address or an entire subnet

Uses concurrent ICMP pings for faster scanning

Displays:

Active hosts

Total hosts scanned

Scan duration

Built with Python and icmplib

Requirements

Python 3.8+

icmplib library

Administrator/root privileges may be required to send ICMP packets

Install dependencies:

pip install icmplib

How It Works

The user enters an IP address or subnet (CIDR notation).

The program generates all usable host IPs in the subnet.

Each host is pinged multiple times using multiping.

Hosts that respond are marked as alive.

The program outputs scan results and timing information.

Usage

Run the script:

python ping_scanner.py


You will be prompted for input:

Please enter the ip address or subnet: 192.168.1.0/24
Please enter number of times to ping: 2

Example Output
This addresses are being scanned:  192.168.1.0/24
[Host(address='192.168.1.1'), Host(address='192.168.1.5')]
2 Hosts are up
254 Hosts scanned
This scan took 1.42 seconds

Notes & Limitations

Hosts that block ICMP traffic may appear as down even if they are online.

Large subnets may take longer to scan depending on system resources.

High concurrency (concurrent_tasks=400) may not be suitable for all environments.

Output currently prints raw Host objects; formatting can be improved for readability.

Permissions

On some systems, ICMP requires elevated privileges:

Linux / macOS: Run with sudo

Windows: Run as Administrator

Legal Disclaimer

This tool is intended for educational purposes and authorized network testing only.
Do not scan networks or devices without explicit permission.

Future Improvements (Optional)

Pretty-print live hosts

Export results to a file (TXT/CSV/JSON)

Add command-line arguments instead of input()

Error handling for invalid IPs or subnets

License

This project is released under the MIT License.
