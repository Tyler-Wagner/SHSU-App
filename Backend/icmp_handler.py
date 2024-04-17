import scapy.all as scapy
<<<<<<< Updated upstream
ICMPcount = 0
=======
#global ICMPcount
#ICMPcount = 0

>>>>>>> Stashed changes
class CheckICMP():
    def __init__(self, packet, src_ip, dst_ip):
        self.packet = packet
        self.src_ip = src_ip
        self.dst_ip = dst_ip

    def handle_icmp_packet(self):
        ICMPcount + 1
        #print("Got packet")# used for debugging
<<<<<<< Updated upstream

=======
        #ICMPcount+=1
>>>>>>> Stashed changes
        if self.packet.haslayer(scapy.ICMP):
            # Extracting the ICMP information
            icmp_layer = self.packet[scapy.ICMP]

            #displaying information to the CONSOLE
            print(f"ICMP: {self.src_ip} -> {self.dst_ip}")

            

        else:
            print("Not seeing ICMP")
<<<<<<< Updated upstream
    def ICMPPacketCount(self):
        return ICMPcount
=======
            
    #def get_ICMP_count():
        #return ICMPcount

>>>>>>> Stashed changes
