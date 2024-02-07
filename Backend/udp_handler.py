import scapy.all as scapy

# This is what we call whenever we send the packet to get broken down by the system
# Basically an init
def handle_udp_packet(packet, src_ip, src_port, dst_ip, dst_port):
    #print("Got packet")# used for debugging


    if packet.haslayer(scapy.UDP):
        # Extracting the TCP information
        udp_layer = packet[scapy.UDP]

        #accessing the header fields
        seq_number = udp_layer.seq
        ack_number = udp_layer.ack
        flags = figure_flag(udp_layer.flags)

        

        #displaying information to the CONSOLE
        print(f"UDP: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
        print(f"Sequence Number: {seq_number}")
        print(f"Acknowledgement Number: {ack_number}")
        print(f"Flags: {flags}")

    else:
        print("Not seeing UDP")

"""
Takes the information from scapy's flag and makes it easier for us to read
when we are trying to move it to the front end and read it there I would use the raw flag at first
THEN proceed to implement the below
"""        
def figure_flag(raw_flag):
    n_flag = ""
    match raw_flag:
        case 'F':
            n_flag = 'FIN'
        case 'S':
            n_flag = 'SYN'
        case 'R':
            n_flag = 'RST'
        case 'P':
            n_flag = 'PSH'
        case 'A':
            n_flag = 'ACK'
        case 'U':
            n_flag = 'URG'
        case 'E':
            n_flag = 'ECE'
        case 'C':
            n_flag ='CWR'
        case _:
            print("Not implemented yet")
    return n_flag
