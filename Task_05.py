pip install scapy

from scapy.all import *
import datetime

def packet_callback(packet):
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Basic packet information
    source_ip = packet[IP].src if IP in packet else "N/A"
    dest_ip = packet[IP].dst if IP in packet else "N/A"
    protocol = packet[IP].proto if IP in packet else "N/A"

    # Get the payload data
    payload = packet.load if Raw in packet else "N/A"

    # Print packet information
    print(f"[{timestamp}] {source_ip} -> {dest_ip} | Protocol: {protocol} | Payload: {payload}")

def main():
    # Start sniffing packets
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, filter="ip", store=0)

if __name__ == "__main__":
    main()
