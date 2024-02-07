import psutil
import scapy.all as scapy
from tcp_handler import handle_tcp_packet

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
        #print(f"IP Packet: {src_ip} -> {dst_ip}")

        #check the kind of packet that was being sent
        if packet.haslayer(scapy.TCP):
            src_port = packet[scapy.TCP].sport
            dst_port = packet[scapy.TCP].dport
            #use the below for debugging in the visual mode
            #print(f"TCP Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

            #send everything to the correct file below
            handle_tcp_packet(packet, src_ip, src_port, dst_ip, dst_port)
        
        elif packet.haslayer(scapy.UDP):
            src_port = packet[scapy.UDP].sport
            dst_port = packet[scapy.UDP].dport
            print(f"UDP Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

            #send everything to the correct file below
        
        elif packet.haslayer(scapy.ICMP):
            src_port = packet[scapy.ICMP].sport
            dst_port = packet[scapy.ICMP].dport
            print(f"ICMP Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

            #send everything to the correct file below

    #APR is the only thing that doesn't have te IP filter in scapy
    elif packet.haslayer(scapy.ARP):
        src_ip = packet[scapy.ARP].psrc
        dst_ip = packet[scapy.ARP].pdst
        print(f"ARP Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

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
