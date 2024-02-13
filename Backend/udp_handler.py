import scapy.all as scapy

# This is what we call whenever we send the packet to get broken down by the system
# Basically an init
def handle_udp_packet(packet, src_ip, src_port, dst_ip, dst_port):
    #print("Got packet")# used for debugging


    if packet.haslayer(scapy.UDP):
        # Extracting the TCP information
        udp_layer = packet[scapy.UDP]

        #displaying information to the CONSOLE
        print(f"UDP: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")



    else:
        print("Not seeing UDP")
