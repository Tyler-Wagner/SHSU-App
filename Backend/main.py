import psutil
import scapy.all as scapy
from tcp_handler import * #change this to only import the needed class
from udp_handler import * #change this to only import the needed class
from icmp_handler import * #change this to only import the needed class
from arp_handler import CheckARP

def list_network_devices():
    # Get a list of all network devices using psutil
    devices = psutil.net_if_addrs()
    
    print("Network Devices:")
    for index, (name, addresses) in enumerate(devices.items()):
        print(f"{index + 1}. {name}")
        print("   Addresses:")
        for addr in addresses:
            print(f"      {addr.family.name}: {addr.address}")

def process_packet(packet):
    # Process and display information about the packet
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        print(f"IP Packet: {src_ip} -> {dst_ip}")
        
        #checking for protocols below
        if packet.haslayer(scapy.TCP):
            src_port = packet[scapy.TCP].sport
            dst_port = packet[scapy.TCP].dport
            # TCP ANALYZER HERE
            handle_tcp_packet(packet, src_ip, src_port, dst_ip, dst_port)

        elif packet.haslayer(scapy.UDP):
            src_port = packet[scapy.UDP].sport
            dst_port = packet[scapy.UDP].dport
            # UDP ANALYZER HERE
            handle_udp_packet(packet, src_ip, src_port, dst_ip, dst_port)

        elif packet.haslayer(scapy.ICMP):
            icmp_type = packet[scapy.ICMP].type
            # ICMP ANALYZER HERE
            handle_icmp_packet(packet, src_ip, dst_ip)


    elif packet.haslayer(scapy.ARP):
        src_ip = packet[scapy.ARP].psrc
        dst_ip = packet[scapy.ARP].pdst
        src_mac = packet[scapy.ARP].hwsrc
        dst_mac = packet[scapy.ARP].hwdst
        # use the below for debugging
        print(f"ARP Packet: {src_ip} -> {dst_ip}")
        # ANALYZE HERE
        arp_packet_check = CheckARP(packet, src_ip, src_mac, dst_ip, dst_mac)
        arp_packet_check.handle_arp_packet()
    
def capture_packets(interface):
    print(f"\nCapturing packets on {interface}...\n")
    scapy.sniff(iface=interface, store=False, prn=process_packet)

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
