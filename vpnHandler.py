from os import system
import argparse
import sys

def openVPN():
    print("Opening VPN...")
    system('sudo openvpn /etc/openvpn/ovpn_udp/us842.nordvpn.com.udp.ovpn')
    
def closeVPN():
    print("Closing VPN...")
    os.system('pkill -f /Users/jackwarr/Documents/createBotNetwork.py')

def checkVPN():
    print("Checking VPN...")
    
def closing():
    closeVPN()
    
parser = argparse.ArgumentParser(description="Does some awesome things.")
parser.add_argument('message', type=str, help="pass a message into the script")


if __name__ == '__main__':
    args = parser.parse_args(sys.argv[1:])
    #print args.message
    if str(args.message) == "openVPN":
        openVPN()
    elif str(args.message) == "closeVPN":
        closeVPN()
    else:
        print("UNKNOWN COMMAND")
