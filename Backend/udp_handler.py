import scapy.all as scapy
<<<<<<< Updated upstream
UDPcount = 0
=======
#global UDPcount
#UDPcount = 0
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
=======
        #UDP_count+=1
>>>>>>> Stashed changes

        # check to see if I sent the right layer through
        if self.packet.haslayer(scapy.UDP):
            # Extracting the TCP information
            udp_layer = self.packet[scapy.UDP]

            #displaying information to the CONSOLE
            print(f"UDP: {self.src_ip}:{self.src_port} -> {self.dst_ip}:{self.dst_port}")

        else:
            print("Not seeing UDP")
<<<<<<< Updated upstream
    def UDPPacketCount(self):
        return UDPcount
=======
   #def get_UDPcount(UDPcount):
        #return UDPcount
>>>>>>> Stashed changes
#FORCING AN UPDATE