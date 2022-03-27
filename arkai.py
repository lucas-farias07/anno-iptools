#general
import pyfiglet
import ipaddress
import requests
import socket
import time
import sys
import os

os.system("cls")

banner = pyfiglet.figlet_format('Arkai', font= 'alligator')
author = pyfiglet.figlet_format('ANOO')

print('''\u001b[32;1m

''')
print(banner)
print('''

────── ANOO's Arkai ─────────────────────────────────────────
    Arkai is a IP/Server sniffer made by ANOO.
    Use only for educational purposes.

        sniff [-i] [-p]
        -i: IP address
        -p: sniff ports (True or False)
        -#:



''')
use = str(input('->  '))
o_u = []
o_u = use.split()
## NOTE:
# o_u[0] = 'sniff' // o_u[1] = ip // o_u[2] = sniff ports or no
sniff = o_u[0]
ip = o_u[1]
port = o_u[2]

if o_u[0] == 'sniff':
    if port == 'False':
        def ipv(ip_addr):
            try:
                ipaddress.ip_address(ip_addr)
                return True
            except ValueError:
                return False

        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        if (ipv(ip)):
            print(ip, 'is valid.')
        else:
            print(ip, 'is invalid.')

        print('Gathering the sniffed info...')
        time.sleep(2)

        url = "http://ip-api.com/json/{0}"
        response = requests.get(url.format(ip)).json()
        for key in response:
            print("{0: <15} - {1}".format(key, response[key]))
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

        time.sleep(2)
    else:
        pass

    if port == 'True':
        def ipv(ip_addr):
            try:
                ipaddress.ip_address(ip_addr)
                return True
            except ValueError:
                return False

        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        if (ipv(ip)):
            print(ip, 'is valid.')
        else:
            print(ip, 'is invalid.')

        print('Gathering the sniffed info...')
        time.sleep(2)

        url = "http://ip-api.com/json/{0}"
        response = requests.get(url.format(ip)).json()
        for key in response:
            print("{0: <15} - {1}".format(key, response[key]))

        target = ip
        print()
        print('Now looking for open ports:')
        print()
        try:
            for port in range(1,65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)

                # returns an error indicator
                result = s.connect_ex((target,port))
                if result ==0:
                    print("Port {} is open to public".format(port))
                s.close()
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        except KeyboardInterrupt:
                print("\n Exiting Program !!!!")
                sys.exit()
        except socket.gaierror:
                print("\n Hostname Could Not Be Resolved !!!!")
                sys.exit()
        except socket.error:
                print("\ Server not responding !!!!")
                sys.exit()

        time.sleep(2)
    else:
        pass
else:
    pass
