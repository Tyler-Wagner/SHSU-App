#MIC IMPORTS
import scapy.all as scapy
import os
import sys
import time
import pyautogui
#BACKEND IMPORTS
from Backend.tcp_handler import CheckTCP
from Backend.udp_handler import CheckUDP
from Backend.icmp_handler import CheckICMP
from Backend.arp_handler import CheckARP
#HANDLER IMPORTS
from Handlers.dbHandle import setPacketCounter, getPacketCounter

flag = False #Tell Capture Packets to stop

def kill_cmd():
    # Simulate Ctrl+C key press to send KeyboardInterrupt signal to the command prompt
    global flag
    flag = True
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    os.system("taskkill /F /IM cmd.exe")
    sys.exit()

def process_packet(packet, data_handler):
    # Process and display information about the packet
    global flag
    if flag == True:
        return
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst

        if packet.haslayer(scapy.TCP):
            src_port = packet[scapy.TCP].sport
            dst_port = packet[scapy.TCP].dport
            tcp_packet_check = CheckTCP(packet, src_ip, src_port, dst_ip, dst_port)# creates instance
            tcp_packet_check.handle_tcp_packet() # calls instance
            TCPcount = getPacketCounter("TCP")
            TCPcount+=1
            setPacketCounter("TCP", TCPcount)
            data_handler.add_log_row("TCP", f"Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")# sends to data handler
            data_handler.add_tableWidgetle_row(src_ip, src_port, "TCP")


        elif packet.haslayer(scapy.UDP):
            src_port = packet[scapy.UDP].sport
            dst_port = packet[scapy.UDP].dport
            UDPcount=getPacketCounter("UDP")
            UDPcount+=1
            setPacketCounter("UDP", UDPcount)

            udp_packet_check = CheckUDP(packet, src_ip, src_port, dst_ip, dst_port)# creates instance
            udp_packet_check.handle_udp_packet() # calls instance
            data_handler.add_log_row("UDP", f"Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
            data_handler.add_tableWidgetle_row(src_ip, src_port, "UDP")

        elif packet.haslayer(scapy.ICMP):
            icmp_type = packet[scapy.ICMP].type
            data_handler.add_log_row("ICMP", f"Packet: {src_ip} -> {dst_ip}") # ICMP does not have ports
            # Call any other processing function for ICMP packets here if needed
            ICMPcount = getPacketCounter("ICMP")
            ICMPcount+=1
            setPacketCounter("ICMP", ICMPcount)
            ICMP_packet_check = CheckICMP(packet, src_ip, icmp_type)# creates instance
            ICMP_packet_check.handle_icmp_packet() # calls instance
            data_handler.add_tableWidgetle_row(src_ip, -1, "ICMP")

    elif packet.haslayer(scapy.ARP):
        src_ip = packet[scapy.ARP].psrc
        dst_ip = packet[scapy.ARP].pdst
        src_mac = packet[scapy.ARP].hwsrc
        dst_mac = packet[scapy.ARP].hwdst
        ARPcount = getPacketCounter("ARP")
        ARPcount+=1
        setPacketCounter("ARP", ARPcount)
        ARP_packet_check = CheckARP(data_handler, packet, src_ip, src_mac, dst_ip, dst_mac)# creates instance
        data_handler.add_log_row("ARP", f"sIP: {src_ip} dIP: {dst_ip} sMAC: {src_mac}")
        data_handler.add_tableWidgetle_row(src_ip, -1, "ARP")
        ARP_packet_check.handle_arp_packet() # calls instance


# Modify the call to process_packet in capture_packets
def capture_packets(interface, data_handler):
    scapy.sniff(iface=interface, store=False, prn=lambda x: process_packet(x, data_handler))