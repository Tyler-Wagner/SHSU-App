import scapy.all as scapy

# This is what we call whenever we send the packet to get broken down by the system
# Basically an init
def handle_tcp_packet(packet, src_ip, src_port, dst_ip, dst_port):
    #print("Got packet")# used for debugging


    if packet.haslayer(scapy.TCP):
        # Extracting the TCP information
        tcp_layer = packet[scapy.TCP]

        #accessing the header fields
        seq_number = tcp_layer.seq
        ack_number = tcp_layer.ack
        flags = figure_flag(tcp_layer.flags)

        

        #displaying information to the CONSOLE
        print(f"TCP: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
        print(f"Sequence Number: {seq_number}")
        print(f"Acknowledgement Number: {ack_number}")
        print(f"Flags: {flags}")

    else:
        print("Not seeing TCP")

def figure_flag(raw_flag):
    n_flag = ""
    match raw_flag:
        case 'F':
            n_flag = 'FIN'
        case 'S':
            n_flag = 'SYN'
        case '':

