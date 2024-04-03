import sys
import os
import psutil
import scapy.all as scapy
# from Backend.tcp_handler import handle_tcp_packet
# from Backend.udp_handler import handle_udp_packet
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtCore import QTimer
# from time import sleep # FOR SIMULATION


def list_network_devices():
    # Get a list of all network devices using psutil
    devices = psutil.net_if_addrs()
    
    print("Network Devices:")
    for index, (name, addresses) in enumerate(devices.items()):
        print(f"{index + 1}. {name}")
        print("   Addresses:")
        for addr in addresses:
            print(f"      {addr.family.name}: {addr.address}")

def process_packet(packet, data_handler):
    # Process and display information about the packet
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst

        if packet.haslayer(scapy.TCP):
            src_port = packet[scapy.TCP].sport
            dst_port = packet[scapy.TCP].dport
            data_handler.add_log_row("TCP", f"Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")


            # Call handle_tcp_packet or any other processing function here if needed
            # handle_tcp_packet(packet, src_ip, src_port, dst_ip, dst_port)

        elif packet.haslayer(scapy.UDP):
            src_port = packet[scapy.UDP].sport
            dst_port = packet[scapy.UDP].dport
            data_handler.add_log_row("UDP", f"Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

            # Call handle_udp_packet or any other processing function here if needed
            # handle_udp_packet(packet, src_ip, src_port, dst_ip, dst_port)

        elif packet.haslayer(scapy.ICMP):
            src_port = packet[scapy.ICMP].sport
            dst_port = packet[scapy.ICMP].dport
            data_handler.add_log_row("ICMP", f"Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

            # Call any other processing function for ICMP packets here if needed

    elif packet.haslayer(scapy.ARP):
        src_ip = packet[scapy.ARP].psrc
        dst_ip = packet[scapy.ARP].pdst
        data_handler.add_log_row("ARP", f"Packet: {src_ip} -> {dst_ip}")

        # Call any other processing function for ARP packets here if needed

# Modify the call to process_packet in capture_packets
def capture_packets(interface, data_handler):
    print(f"\nCapturing packets on {interface}...\n")
    scapy.sniff(iface=interface, store=False, prn=lambda x: process_packet(x, data_handler))

def main():
    list_network_devices()

    # Prompt the user to choose a network device
    choice = int(input("Enter the number of the interface you want to capture packets on: "))

    # Get a list of all network devices again
    devices = list(psutil.net_if_addrs().keys())

    if 1 <= choice <= len(devices):
        selected_interface = devices[choice - 1]
        capture_packets(selected_interface)
    else:
        print("Invalid choice. Please choose a valid interface.")

if __name__ == "__main__":
    main()
