#!/usr/bin/env python3
"""
Python Ping Scanner with CSV Export
Description: Scan a single IP or subnet using ICMP pings and export live hosts to CSV.
Requirements: icmplib
"""

import ipaddress
import time
import csv
from icmplib import multiping


def get_target_ips():
    """Prompt user for target IP/subnet and return list of host IPs."""
    while True:
        address = input("Please enter the IP address or subnet (e.g., 192.168.1.0/24): ").strip()
        try:
            subnet = ipaddress.ip_network(address, strict=False)
            ip_list = [str(ip) for ip in subnet.hosts()]
            return ip_list
        except ValueError:
            print("Invalid IP or subnet. Please try again.")


def get_ping_count():
    """Prompt user for number of ping attempts."""
    while True:
        count = input("Please enter number of times to ping (default 2): ").strip()
        if count == '':
            return 2
        if count.isdigit() and int(count) > 0:
            return int(count)
        print("Please enter a valid positive integer.")


def ping_hosts(ip_list, count, concurrency=400):
    """Ping all IPs concurrently and return a list of alive hosts."""
    print(f"\nScanning {len(ip_list)} hosts...")
    start_time = time.time()
    hosts = multiping(ip_list, count=count, concurrent_tasks=concurrency)
    alive_hosts = [host.address for host in hosts if host.is_alive]
    end_time = time.time()
    print(f"Scan completed in {end_time - start_time:.2f} seconds.")
    print(f"{len(alive_hosts)} hosts are up out of {len(ip_list)} scanned.\n")
    return alive_hosts


def save_to_csv(host_list, filename="alive_hosts.csv"):
    """Save alive hosts to a CSV file."""
    if not host_list:
        print("No hosts to save.")
        return
    try:
        with open(filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["IP Address"])
            for host in host_list:
                writer.writerow([host])
        print(f"Alive hosts saved to '{filename}'.")
    except Exception as e:
        print(f"Error saving to CSV: {e}")


def main():
    ip_list = get_target_ips()
    ping_count = get_ping_count()
    alive_hosts = ping_hosts(ip_list, ping_count)
    if alive_hosts:
        print("Alive Hosts:")
        for host in alive_hosts:
            print(host)
    save_to_csv(alive_hosts)


if __name__ == "__main__":
    main()
