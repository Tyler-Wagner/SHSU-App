# Should work but not sure as I cannot
# test it. Need to make sure but if it does
# it only works for Windows and not Linux
# Linux has too many firewalls and I do not
# have the time to get that implemented

import subprocess

def add_firewall_rule(port, protocol, choice):

    try:
        if choice == True:
            # Example: Add an inbound rule to allow traffic on a specific port
            subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                            'name=AllowPort', 'dir=in', 'action=allow',
                            f'protocol={protocol}', f'localport={port}'])
        else:
            # Example: Add an inbound rule to allow traffic on a specific port
            subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                            'name=DenyPort', 'dir=in', 'action=allow',
                            f'protocol={protocol}', f'localport={port}'])
    except subprocess.CalledProcessError as e:
        print(f"Error executing subprocess command {e}") # MAKE THIS GO TO THE GUI

    