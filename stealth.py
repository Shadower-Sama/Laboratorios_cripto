from scapy.all import IP, ICMP, send

def send_icmp_data(destination, data):
    # Split the data into individual characters
    for char in data:
        # Create an IP packet with an ICMP layer
        packet = IP(dst=destination)/ICMP()/char.encode()
        # Send the packet
        send(packet, verbose=0)

# User input for the text and the destination IP address
text = input("Enter the text to be sent: ")
destination_ip = input("Enter the destination IP address: ")

# Send each character in an ICMP packet
send_icmp_data(destination_ip, text)

print(f"Data sent to {destination_ip}")
