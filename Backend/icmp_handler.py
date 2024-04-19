import scapy.all as scapy

class CheckICMP():
    def __init__(self, packet, src_ip, dst_ip):
        self.packet = packet
        self.src_ip = src_ip
        self.dst_ip = dst_ip

    def handle_icmp_packet(self):
        if self.packet.haslayer(scapy.ICMP):
            # Extracting the ICMP information
            icmp_layer = self.packet[scapy.ICMP]

        else:
            pass