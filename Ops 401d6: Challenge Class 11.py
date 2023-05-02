# Imports all functions and classes from the Scapy library.
from scapy.all import *

# Defines host IP and port range for the scan
target_ip = "scanme.nmap.org"
port_range = range(1, 100)

# Iterate over the ports and send SYN packets
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
        print(f"Port {port} is open.")
    elif response is not None and response.haslayer(TCP) and response[TCP].flags == 0x14:
        print(f"Port {port} is closed.")
    else:
        print(f"Port {port} is filtered and silently dropped.")
