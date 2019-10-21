#!/usr/bin/env python

import subprocess
import optparse


# subprocess.call("date >> ~/Desktop/pehp/comdlog.txt", shell=True)
# subprocess.call("ifconfig >> ~/Desktop/pehp/comdlog.txt", shell=True)

#######################
# code from here

parser = optparse.OptionParser()

parser.add_option("-i","--interface", dest="interface", help=" Interface to change mac address")
parser.add_option("-m","--mac", dest="new_mac", help=" new mac address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] Changing mac address for " + interface + " to "+ new_mac)

# subprocess.call("ifconfig "+ interface+" down", shell=True)
# subprocess.call("ifconfig "+ interface+" hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig "+ interface+" up", shell=True)
