// all imports needed
#include <pcap.h>
#include <iostream>

using namespace std;

void packet_handler(u_char* user, const struct pcap_pkthdr* pkthdr, const u_char* packet)
{
    //process the captured packet here
    //pkthdr contains information about the packet
    //packet is a pointer to the packet data
    //user can be sed to pass user-specific data (nullptr in this example)

    cout << "Captured a Packet!";
}

int main()
{
    pcap_t* pcap_handle;
    char errbuff[PCAP_ERRBUF_SIZE];

    //open the network device for capture
    pcap_handle = pcap_open_live("eth0", BUFSIZ, 1, 1000, errbuff);

    if (pcap_handle == nullptr)
    {
        cerr << "Error opening device for capture" << errbuff;
        return 1;
    }

    //set a packet capture filter (this can be optional HOWEVER we will probably want to do this)
    struct bpf_program fp;

    if (pcap_compile(pcap_handle, &fp, "tcp", 0, PCAP_NETMASK_UNKNOWN) == -1)
    {
        cerr << "erro compiling the filter";
    }

    if(pcap_setfilter(pcap_handle, &fp) == -1)
    {
        cerr << "Error setting filter"; 
    }

    pcap_loop(pcap_handle, 0, packet_handler, nullptr);

    pcap_close(pcap_handle);

    return 0;
}

