import scapy.all as scapy
UDPcount = 0
class CheckUDP:

    def __init__(self, packet, src_ip, src_port, dst_ip, dst_port):
        self.packet = packet
        self.src_ip = src_ip
        self.src_port = src_port
        self.dst_ip = dst_ip
        self.dst_port = dst_port
    
    def handle_udp_packet(self):
        UDPcount + 1
        #print("Got packet")# used for debugging

        # check to see if I sent the right layer through
        if self.packet.haslayer(scapy.UDP):
            # Extracting the TCP information
            udp_layer = self.packet[scapy.UDP]

            #displaying information to the CONSOLE
            # print(f"UDP: {self.src_ip}:{self.src_port} -> {self.dst_ip}:{self.dst_port}")

        else:
            print("Not seeing UDP")
    def UDPPacketCount(self):
        return UDPcount