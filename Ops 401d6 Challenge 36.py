import subprocess

# Prompt user for target address and port
target_address = input("Enter the target address (URL or IP): ")
target_port = input("Enter the target port number: ")

# Perform banner grabbing using netcat
print("Banner grabbing using netcat:")
nc_command = f"nc {target_address} {target_port}"
nc_output = subprocess.run(nc_command, shell=True, capture_output=True, text=True)
print(nc_output.stdout)

# Perform banner grabbing using telnet
print("Banner grabbing using telnet:")
telnet_command = f"telnet {target_address} {target_port}"
telnet_output = subprocess.run(telnet_command, shell=True, capture_output=True, text=True)
print(telnet_output.stdout)

# Perform banner grabbing using Nmap
print("Banner grabbing using Nmap:")
nmap_command = f"nmap -p1-65535 -sV {target_address}"
nmap_output = subprocess.run(nmap_command, shell=True, capture_output=True, text=True)
print(nmap_output.stdout)
