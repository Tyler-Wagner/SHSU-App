import sys
import os
import psutil
import scapy.all as scapy
from Backend.tcp_handler import handle_tcp_packet as CheckTCP
from Backend.udp_handler import handle_udp_packet as CheckUDP
from Backend.icmp_handler import handle_icmp_packet as CheckICMP
#from Handlers.sendNotification import sendnotification

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
            tcp_packet_check = CheckTCP(packet, src_ip, src_port, dst_ip, dst_port)# creates instance
            tcp_packet_check.handle_tcp_packet() # calls instance
            data_handler.add_log_row("TCP", f"{src_ip}:{src_port} -> {dst_ip}:{dst_port}")# sends to data handler

        elif packet.haslayer(scapy.UDP):
            src_port = packet[scapy.UDP].sport
            dst_port = packet[scapy.UDP].dport

            udp_packet_check = CheckUDP(packet, src_ip, src_port, dst_ip, dst_port)# creates instance
            udp_packet_check.handle_udp_packet() # calls instance
            data_handler.add_log_row("UDP", f"{src_ip}:{src_port} -> {dst_ip}:{dst_port}")# sends to data handler

        elif packet.haslayer(scapy.ICMP):
            icmp_type = packet[scapy.ICMP].type
            # data_handler.add_log_row("ICMP", f"{src_ip} -> {dst_ip}") # ICMP does not have ports # sends to data handler
            # Call any other processing function for ICMP packets here if needed
            ICMP_packet_check = CheckICMP(packet, src_ip, icmp_type)# creates instance
            ICMP_packet_check.handle_icmp_packet() # calls instance


  ##  elif packet.haslayer(scapy.ARP):
  #      src_ip = packet[scapy.ARP].psrc
   #     dst_ip = packet[scapy.ARP].pdst
    #    src_mac = packet[scapy.ARP].hwsrc
     #   dst_mac = packet[scapy.ARP].hwdst
      # ARP_packet_check.handle_arp_packet() # calls instance


# Modify the call to process_packet in capture_packets
def capture_packets(interface, data_handler):
    print(f"\nCapturing packets on {interface}...\n")
    #TEST ATTACK##############################################################################################################
    data_handler.add_current_alerts_row("1234556789",22,22)
    #sendnotification("Attack Detected", f"Please see ALerts Page for the following attack\nIP: 1234556789 SrcP: 22 dstP: 22")
    ##########################################################################################################################
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
