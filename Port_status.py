# Ops Challenge 11
# David Armstrong
# 10/19/2020
# To determine the status of ports at a target

### LIBRARIES ###
from scapy.all import IP, sr1, TCP
import random

### VARIABLES ###
# Define target host
host = "scanme.nmap.org"
# Ports to scan
dport_range = [20, 21, 22, 80, 443]

### FUNCTIONS ###
# Find port status of the target
def port_stat():
    for dst_port in dport_range:
        # Randomized source port
        src_port = random.randint(1000, 10000)
        print("Sending request to port", dst_port, "@", host, "from port", src_port)
        # Sends a SYN request and receives a flag from the target
        response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dport_range,flags="S"),timeout=1,verbose=0)
        # Determine if there is a response
        if response is None:
            print("This port is filtered.")
        # Determine if the response as a TCP attribute
        elif (response.haslayer(TCP)):
            flag = (response.getlayer(TCP).flags)
            # If flags were SYN and ACK
            if (flag == "SA"):
                sr1(IP(dst=host)/TCP(sport=src_port,dport=dport_range,flags="F"),timeout=1,verbose=0)
                print("This port is open.")
            # If flags were Reset and ACK
            elif (flag == "RA"):
                print("This port is closed.")                
        else:
            print("The response was not of protocol type TCP.")

### MAIN ###
port_stat()
### END ###
