import scapy.all as scapy

class CheckTCP:
    def __init__(self, packet, src_ip, src_port, dst_ip, dst_port):
        self.packet = packet
        self.src_ip = src_ip
        self.src_port = src_port
        self.dst_ip = dst_ip
        self.dst_port = dst_port

    def handle_tcp_packet(self):
        #print("Got packet")# used for debugging

        # check to see if I sent the right layer through
        if self.packet.haslayer(scapy.TCP):
            # Extracting the TCP information
            tcp_layer = self. packet[scapy.TCP]

            #accessing the header fields
            seq_number = tcp_layer.seq
            ack_number = tcp_layer.ack
            flags = self.figure_flag(tcp_layer.flags)

            

            #displaying information to the CONSOLE
            print(f"TCP: {self.src_ip}:{self.src_port} -> {self.dst_ip}:{self.dst_port}")
            print(f"Sequence Number: {seq_number}")
            print(f"Acknowledgement Number: {ack_number}")
            print(f"Flags: {flags}")

        else:
            print("Not seeing TCP")

    """
    Takes the information from scapy's flag and makes it easier for us to read
    when we are trying to move it to the front end and read it there I would use the raw flag at first
    THEN proceed to implement the below
    """        
    def figure_flag(self, raw_flag):
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
            case 'FA':
                n_flag = 'FINACK'
            case 'PA':
                n_flag = 'PUSH_ACK'
            case 'SA':
                n_flag = 'SYNACK'
            case 'RA':
                n_flag = 'RSTACK'
            case _:
                print(f"TCP flag, {raw_flag} not implemented yet")
        return n_flag

#FORCING AN UPDATE