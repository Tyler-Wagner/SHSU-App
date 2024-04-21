# Snort rules parser

import re

# Define a class to store rule details
class SnortRule:
    def __init__(self, action, protocol, src_ip, src_port, direction, dst_ip, dst_port, options):
        self.action = action
        self.protocol = protocol
        self.src_ip = src_ip
        self.src_port = src_port
        self.direction = direction
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.options = options

    def __repr__(self):
        return f"{self.action} {self.protocol} {self.src_ip} {self.src_port} {self.direction} {self.dst_ip} {self.dst_port} {self.options}"

# Function to parse a single Snort rule
def parse_rule(rule):
    pattern = r'(\w+)\s+(\w+)\s+([\w\./]+)\s+(\w+)\s+(\W+)\s+([\w\./]+)\s+(\w+)\s+\((.*?)\)'
    match = re.match(pattern, rule.strip())
    if match:
        return SnortRule(*match.groups())
    else:
        return None

# Function to parse a file containing Snort rules
def parse_rules_file(filename):
    rules = []
    with open(filename, 'r') as file:
        for line in file:
            rule = parse_rule(line)
            if rule:
                rules.append(rule)
    return rules