import scapy.all as scapy

class CheckUDP:

    def __init__(self, packet, src_ip, src_port, dst_ip, dst_port):
        self.packet = packet
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.dst_port = dst_port
    
    def handle_udp_packet(packet, src_ip, src_port, dst_ip, dst_port):
        #print("Got packet")# used for debugging

        # check to see if I sent the right layer through
        if packet.haslayer(scapy.UDP):
            # Extracting the TCP information
            udp_layer = packet[scapy.UDP]

            #displaying information to the CONSOLE
            print(f"UDP: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

        else:
            print("Not seeing UDP")

#FORCING AN UPDATE