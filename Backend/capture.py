from scapy.all import sniff
import IOdevices

def packet_handler(pkt):
    #all packet analysis will happen in here
    print("Packet Captured!")



def run():
    # backend main to test in a terminal for the time being.

    #below should list all network devices on the device
    deviceslist = []


    capChoice = input(f"Please select which interface you would like to capture on")


if __name__ == "__main__":
    run()