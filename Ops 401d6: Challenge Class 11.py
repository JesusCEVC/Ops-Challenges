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

def network_scanner(target_ip):
    # Send ICMP echo request to check if host is responsive
    response = sr1(IP(dst=target_ip)/ICMP(), timeout=1, verbose=0)

    if response is None:
        print(f"Host {target_ip} is down/unresponsive.")
    elif response.type == 3 and response.code in [1, 2, 3, 9, 10, 13]:
        print(f"Host {target_ip} is actively blocking ICMP traffic.")
    else:
        print(f"Host {target_ip} is responding.")
        port_range = range(1, 1001)
        open_ports = tcp_port_scan(target_ip, port_range)
        print(f"{len(open_ports)} port(s) are open.")
        

# Prompt user for IP address to target
target_ip = input("Enter the IP address to target: ")

# Perform network scanning
network_scanner(target_ip)
