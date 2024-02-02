from scapy.all import sniff
import IOdevices

def packet_handler(pkt):
    print("Packet Captured!")

def run():
    IOdevices.list_network_interfaces()

if __name__ == "__main__":
    run()