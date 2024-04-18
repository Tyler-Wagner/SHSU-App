import scapy.all as scapy

class CheckICMP():
    def __init__(self, packet, src_ip, dst_ip):
        self.packet = packet
        self.src_ip = src_ip
        self.dst_ip = dst_ip

    def handle_icmp_packet(self):
        #ICMPcount + 1
        #print("Got packet")# used for debugging
        if self.packet.haslayer(scapy.ICMP):
            # Extracting the ICMP information
            icmp_layer = self.packet[scapy.ICMP]

            #displaying information to the CONSOLE
            # print(f"ICMP: {self.src_ip} -> {self.dst_ip}")

            

        else:
            # print("Not seeing ICMP")
            pass
            
    #def get_ICMP_count():
        #return ICMPcount