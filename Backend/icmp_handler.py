import scapy.all as scapy

def handle_icmp_packet(packet, src_ip, dst_ip):
    #print("Got packet")# used for debugging


    if packet.haslayer(scapy.ICMP):
        # Extracting the ICMP information
        icmp_layer = packet[scapy.ICMP]

        #displaying information to the CONSOLE
        print(f"UDP: {src_ip} -> {dst_ip}")

        

    else:
        print("Not seeing ICMP")

