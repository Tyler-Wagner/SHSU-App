import psutil

def list_network_interfaces():
    interfaces = psutil.net_if_addrs()

    for interface, addresses in interfaces.items():
        print(f"Interface: {interface}")