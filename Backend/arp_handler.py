import scapy.all as scapy

class CheckARP:
    # allows the class to only use variables within the class
    # basically a constructor
    def __init__(self, packet, src_ip, src_mac, dst_ip, dst_mac):
        self.packet = packet
        self.src_ip = src_ip
        self.src_mac = src_mac
        self.dst_ip = dst_ip
        self.dst_mac = dst_mac

    def handle_arp_packet(self):
        if self.packet.haslayer(scapy.ARP):
            arp_layer = self.packet[scapy.ARP]
            operation = "Request" if arp_layer.op == 1 else "Reply"

            print(f"ARP {operation}: {self.src_ip} ({self.src_mac}) -> {self.dst_ip} ({self.dst_mac})")

        else:
            print("Not seeing ARP")

    def check_for_poison(self):
        pass

#FORCING AN UPDATE