from scapy.all import *

def tcp_port_scan(target_ip, port_range):
    # Iterate over the ports and send SYN packets
    open_ports = []
    for port in port_range:
        # create the SYN packet
        packet = IP(dst=target_ip)/TCP(dport=port, flags="S")

        # send the packet and wait for a response
        response = sr1(packet, timeout=1, verbose=0)

        # check if a response was received and handle accordingly
        if response is not None and response.haslayer(TCP) and response[TCP].flags == 0x12:
            # send RST packet to close the connection gracefully
            rst_packet = IP(dst=target_ip)/TCP(dport=port, flags="R")
            send(rst_packet, verbose=0)
            open_ports.append(port)
            print(f"Port {port} is open.")
        elif response is not None and response.haslayer(TCP) and response[TCP].flags == 0x14:
            print(f"Port {port} is closed.")
        else:
            print(f"Port {port} is filtered and silently dropped.")
    return open_ports

def icmp_ping_sweep(network_address):
    # Create a list of all addresses in the given network
    network = IPv4Network(network_address, strict=False)
    hosts = list(network.hosts())

    # Ping all addresses on the given network except for network address and broadcast address
    online_hosts = []
    for host in hosts:
        if host != network.network_address and host != network.broadcast_address:
            response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
            if response is None:
                print(f"Host {host} is down/unresponsive.")
            elif response.type == 3 and response.code in [1, 2, 3, 9, 10, 13]:
                print(f"Host {host} is actively blocking ICMP traffic.")
            else:
                print(f"Host {host} is responding.")
                online_hosts.append(host)
    
    # Count how many hosts are online and inform the user
    num_online_hosts = len(online_hosts)
    print(f"{num_online_hosts} host(s) are online.")
    return online_hosts

# Prompt user for choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode
mode = input("Enter '1' for TCP Port Range Scanner mode, Enter '2' for ICMP Ping Sweep mode: ")

if mode == "1":
    # Defines host IP and port range for the scan
    target_ip = input("Enter your target IP: ")
    port_range = range(int(input("Enter a starting port number: ")), int(input("Enter an ending port number: "))+1)
    tcp_port_scan(target_ip, port_range)

elif mode == "2":
    # Prompt user for network address including CIDR block
    network_address = input("Enter a network address (CIDR block): ")

    # Perform ICMP Ping Sweep tool
    icmp_ping_sweep(network_address)

else:
    print("Invalid.")
