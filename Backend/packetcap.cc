#include "pcap/pcap.h"
#include <iostream>
#include <iphlpapi.h>
#include <string>
#include<locale>
#include<codecvt>

// For Windows
#ifdef _WIN32
#pragma comment(lib, "IPHLPAPI.lib")
#endif

using namespace std;

string get_interface_name(const char* device_name) {
#ifdef _WIN32
    ULONG flags = GAA_FLAG_INCLUDE_PREFIX;

    // Get the size needed
    ULONG outBufLen = 0;
    GetAdaptersAddresses(AF_UNSPEC, flags, nullptr, nullptr, &outBufLen);

    // Allocate memory
    PIP_ADAPTER_ADDRESSES pAddresses = (PIP_ADAPTER_ADDRESSES)malloc(outBufLen);
    if (pAddresses == nullptr) {
        cerr << "Memory allocation failed." << endl;
        return "";
    }

    // Get the actual data
    DWORD dwRetVal = GetAdaptersAddresses(AF_UNSPEC, flags, nullptr, pAddresses, &outBufLen);
    if (dwRetVal == NO_ERROR) {
        while (pAddresses) {
            if (strcmp(pAddresses->AdapterName, device_name) == 0) {
                wstring ws(pAddresses -> Description);
                wstring_convert<codecvt_utf8<wchar_t>> converter;
                string interface_name = converter.to_bytes(ws);

                free(pAddresses);
                return interface_name;
            }
            pAddresses = pAddresses->Next;
        }
    } else {
        cerr << "GetAdaptersAddresses failed." << endl;
    }

    free(pAddresses);
    return "";
#else
    // For Linux
    string interface_name;

    DIR* dir = opendir("/sys/class/net");
    if (dir != nullptr) {
        struct dirent* ent;
        while ((ent = readdir(dir)) != nullptr) {
            if (ent->d_type == DT_LNK || ent->d_type == DT_DIR) {
                if (strcmp(ent->d_name, device_name) == 0) {
                    interface_name = ent->d_name;
                    break;
                }
            }
        }
        closedir(dir);
    } else {
        cerr << "Failed to open /sys/class/net directory." << endl;
    }

    return interface_name;
#endif
}

void packet_handler(u_char* user, const struct pcap_pkthdr* pkthdr, const u_char* packet)
{
    // Process captured packets here
    // 'pkthdr' will contain any and all information about the packet
    // 'packet' is a pointer to the packet's data
    // 'user' can be used to pass user-specific data (nullptr for now)
    cout << "Captured packet!" << endl; // Take this out later, this is used for debugging
}

int main()
{
    pcap_if_t* alldevs;
    pcap_if_t* dev;
    char errbuf[PCAP_ERRBUF_SIZE];

    // Retrieve the list of available devices
    if (pcap_findalldevs(&alldevs, errbuf) == -1)
    {
        cerr << "Error finding devices" << errbuf << endl;
        return 1;
    }

    // Print the network interfaces for the user
    int i = 0;
    for (dev = alldevs; dev != nullptr; dev = dev->next) {
        cout << i++ << ". " << "Raw Name: " << dev->name << ", Friendly Name: " << get_interface_name(dev->name) << endl;
    }

    // Prompt the user to choose a device.
    // This will later be replaced by a python GUI and a way to communicate between the two at launch
    int choice;
    cout << "Enter the number of the interface you want to capture packets on: ";
    cin >> choice;

    // Find the selected device
    dev = alldevs;
    for (i = 1; i < choice && dev != nullptr; i++)
    {
        dev = dev->next;
    }

    if (dev == nullptr)
    {
        cout << "Invalid choice, please choose again." << endl;
        pcap_freealldevs(alldevs);
        return 1;
    }

    // Open the device that the user wants to capture the packets on.
    pcap_t* pcap_handle = pcap_open_live(dev->name, BUFSIZ, 1, 1000, errbuf);

    // Set a packet capture filter (this is optional but we will more than likely do it since we will be using a local host to communicate between the front and back end for the time being)
    struct bpf_program fp;

    if (pcap_compile(pcap_handle, &fp, "tcp", 0, PCAP_NETMASK_UNKNOWN) == -1)
    {
        cerr << "Error compiling filter." << endl;
        pcap_freealldevs(alldevs);
    }

    if (pcap_setfilter(pcap_handle, &fp) == -1)
    {
        cerr << "Error setting the filter." << endl;
    }

    // Start to capture the packets in a loop
    pcap_loop(pcap_handle, 0, packet_handler, nullptr);

    // Close the handle
    pcap_close(pcap_handle);

    // Free the list of all the devices
    pcap_freealldevs(alldevs);

    return 0;
}