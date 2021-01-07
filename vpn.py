from os import system
import atexit

startVPN():
    print('VPN STARTING...')
    ###########################
    ###########################
    system('sudo openvpn /etc/openvpn/ovpn_udp/us842.nordvpn.com.udp.ovpn')

closeVPN():
    print('VPN CLOSING...')
atexit.register(closeVPN)
