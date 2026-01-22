from icmplib import multiping
import ipaddress
import time
 
# Define the subnet

address = input("Please enter the ip address or subnet: ")

subnet = ipaddress.ip_network(address)

# Start timer
start_time = time.time()
# Create a list of IP addresses in the subnet
ip_list = [str(ip) for ip in subnet.hosts()]

# Number of pings
times_to_ping = input("Please enter number of times to ping: ")
times_to_ping_int = int(times_to_ping)
print(f"This addresses are being scanned: ", {address})

# Ping all IP addresses in the list
start_time = time.time()
hosts = multiping(ip_list, count=times_to_ping_int, concurrent_tasks=400)

# Create an empty list of hosts
host_list = []
# Check the status of each host
for host in hosts:
    if host.is_alive:
        host_list.append(host)
        #print(f'{host.address} is up!')
    else:
        pass

end_time = time.time()

print(host_list)
print(len(host_list), "Hosts are up")
print(len(ip_list), "Hosts scanned")
print("This scan took", end_time - start_time, "seconds")
