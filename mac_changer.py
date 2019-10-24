#!/usr/bin/env python

import subprocess
import optparse
import re
from datetime import datetime  as dt


################################
##########
# Methods and functions definitions here
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help=" Interface to change mac address")
    parser.add_option("-m","--mac", dest="new_mac", help=" new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        #code to handle error
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        #code to handle error
        parser.error("[-] Please specify a new mac address, use --help for more info.")
    return options

def change_mac(interface,new_mac):
    print("[+] Changing mac address for " + interface + " to "+ new_mac)
    # ##################
    # # Not very safe way of execution of system commands while using user input
    # subprocess.call("ifconfig "+ interface+" down", shell=True)
    # subprocess.call("ifconfig "+ interface+" hw ether " + new_mac, shell=True)
    # subprocess.call("ifconfig "+ interface+" up", shell=True)

    # Uncomment this block before using script
    #### To keep track of mac address changes
    log_file = open("./comd_log.txt","a+")
    L = [dt.now().strftime("%Y-%m-%d %H:%M:%S")+"\n", interface + ": " + str(get_current_mac(interface)), "\n \n"]
    log_file.writelines(L)
    log_file.close()
    # subprocess.call("date >> ~/Desktop/pehp/comdlog.txt")
    # subprocess.call(["echo", interface, str(get_current_mac(interface)), ">>","~/Desktop/pehp/comdlog.txt"])

    # Uncomment this block before using script
    ####################
    # Safer way of executing system commands while using user input
    subprocess.call(["ifconfig", interface,"down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

    # check if mac changed or not
    current_mac = get_current_mac(interface)
    if current_mac == new_mac:
        print("[+] Mac address was successfully changed to "+ current_mac)
    else:
        print("[-] Mac address did not get changed.")

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # regex can be created at pythex.org
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read Mac address.")


################################
##########
# Main Code here
# try:
options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current Mac = " + str(current_mac))
change_mac(options.interface, options.new_mac)
# except :
#     print("No such interface. Enter a valid Interface. Run ifconfig or equivalent command to know about available interfaces.")
