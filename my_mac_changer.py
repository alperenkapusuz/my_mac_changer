import subprocess
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
parse_object.add_option("-m","--mac",dest="mac_address",help="new mac address")

(user_inputs, arguments) = parse_object.parse_args()

user_interface = user_inputs.interface
user_mac_address = user_inputs.mac_address

print("my mac changer started!")

#interface = "eth0"
#mac_addres = "00:22:33:77:99:11"

subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
subprocess.call(["ifconfig",user_interface,"up"])

