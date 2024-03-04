import numpy as np

# going to do some counting math in here but brought numpy as a
# helper to do more complex stuff without having to program
# all of that myself

# I more than likely will not need this but its here if I do need it
def packet_math(numUDP, numTCP, numICMP, numARP):
    avgUDP = sum(numUDP,numTCP,numICMP,numARP) / 4