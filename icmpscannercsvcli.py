#!/usr/bin/env python3
"""
Python Ping Scanner with CSV Export (CLI Version)
Author: Frank Casas
Description: Scan a single IP or subnet using ICMP pings and export live hosts to CSV.
Requirements: icmplib
"""

import ipaddress
import time
import csv
import argparse
from icmplib import multiping


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Python Ping Scanner with CSV Export")
    parser.add_argument(
        "-t", "--target", required=True, help="Target IP address or subnet (e.g., 192.168.1.0/24)"
    )
    parser.add_argument(
        "-c", "--count", type=int, default=2, help="Number of times to ping each host (default: 2)"
    )
    parser.add_argument(
        "-o", "--output", default="alive_hosts.csv", help="CSV file to save alive hosts (default: alive_hosts.csv)"
    )
    parser.add_argument(
        "--concurrency", type=int, default=400, help="Number of concurrent pings (default: 400)"
    )
    return parser.parse_args()


def generate_ip_list(target):
    """Generate a list of host IPs from target IP/subnet."""
    try:
        subnet = ipaddress.ip_network(target, strict=False)
        return [str(ip) for ip in subnet.hosts()]
    except ValueError:
        print(f"Invalid IP address or subnet: {target}")
        exit(1)


def ping_hosts(ip_list, count, concurrency):
    """Ping all IPs concurrently and return a list of alive hosts."""
    print(f"Scanning {len(ip_list)} hosts...")
    start_time = time.time()
    hosts = multiping(ip_list, count=count, concurrent_tasks=concurrency)
    alive_hosts = [host.address for host in hosts if host.is_alive]
    end_time = time.time()
    print(f"Scan completed in {end_time - start_time:.2f} seconds.")
    print(f"{len(alive_hosts)} hosts are up out of {len(ip_list)} scanned.\n")
    return alive_hosts


def save_to_csv(host_list, filename):
    """Save alive hosts to a CSV file."""
    if not host_list:
        print("No hosts to save.")
        return
    try:
        with open(filename, mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["IP Address"])
            for host in host_list:
                writer.writerow([host])
        print(f"Alive hosts saved to '{filename}'.")
    except Exception as e:
        print(f"Error saving to CSV: {e}")


def main():
    args = parse_arguments()
    ip_list = generate_ip_list(args.target)
    alive_hosts = ping_hosts(ip_list, args.count, args.concurrency)
    if alive_hosts:
        print("Alive Hosts:")
        for host in alive_hosts:
            print(host)
    save_to_csv(alive_hosts, args.output)


if __name__ == "__main__":
    main()
