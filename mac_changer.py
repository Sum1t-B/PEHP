#!/usr/bin/env python

import subprocess
import optparse


subprocess.call("date >> ~/Desktop/pehp/comdlog.txt", shell=True)
subprocess.call("ifconfig >> ~/Desktop/pehp/comdlog.txt", shell=True)

#######################
# code from here

parser = optparse.OptionParser()


interface = input("interface > ")
new_mac = input("new_mac > ")

print("[+] Changing mac address for " + interface + " to "+ new_mac)

subprocess.call("ifconfig "+ interface+" down", shell=True)
subprocess.call("ifconfig "+ interface+" hw ether " + new_mac, shell=True)
subprocess.call("ifconfig "+ interface+" up", shell=True)
