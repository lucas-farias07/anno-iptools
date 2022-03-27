#python 3.10
#pipenv \Youtube DL\

#hostname info and port scanner
import socket

#sherlock
import webbrowser

#cmd and wifi no stealth sniffing
import subprocess

#ip sniffing
import ipaddress
import requests

#general
import string
import os
import time
import sys
from datetime import datetime

os.system("cls")

print('''\u001b[36;1m
 ____ ____   ____ ____ ____ ____ ____ ____
||R |||E || ||v |||e |||a |||l |||e |||r ||
||__|||__|| ||__|||__|||__|||__|||__|||__||
|/__\|/__\| |/__\|/__\|/__\|/__\|/__\|/__\|
                          \u001b[32;1m
   ┌───────────────────────────────────┐\u001B[36m
   \u001b[32;1m│\u001B[36mAvailable inputs:                  \u001b[32;1m│
   ├─────────────────┬─────────────────┤
   \u001b[32;1m│\u001B[36m0 - hostip       \u001b[32;1m│\u001B[36m1 - sherlock     \u001b[32;1m│
   \u001b[32;1m│\u001B[36m2 - tracert      \u001b[32;1m│\u001B[36m3 - gethistory   \u001b[32;1m│
   \u001b[32;1m│\u001B[36m4 - ipsniff      \u001b[32;1m│\u001B[36m5 - unproc. sniff\u001b[32;1m│
   \u001b[32;1m│\u001B[36m6 - portscan     \u001b[32;1m│\u001B[36m7 -              \u001b[32;1m│
   \u001b[32;1m└─────────────────┴─────────────────┘\u001B[36m


''')
def _main_():
    print('┆')
    input_main = str(input('└─%─> \u001b[32;1m'))

    if input_main == '0':
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print('┌─────────────────────────────────────────────────┐')
        print(' \u001B[36mHost and IP: {}'.format(hostname), '\u001b[32;1m│\u001B[36m', '{}'.format(ip))
        print('\u001b[32;1m└─────────────────────────────────────────────────┘\u001B[36m')
        time.sleep(2)
        _main_()
    else:
        pass

    if input_main == '1':
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print('┌─────────────────────────────────────────────────┐')
        print(' \u001B[36m https://github.com/sherlock-project/sherlock')
        print('\u001b[32;1m└─────────────────────────────────────────────────┘\u001B[36m')
        webbrowser.open('https://github.com/sherlock-project/sherlock', new=2)
        time.sleep(2)
        _main_()
    else:
        pass

    if input_main == '2':
        target = input("Target's IP: ")
        print('┌───────────────────────────────────────────────────────────┐\u001B[36m')
        subprocess.call(['tracert', target])
        print('\u001b[32;1m└───────────────────────────────────────────────────────────┘\u001B[36m')
        time.sleep(2)
        _main_()
    else:
        pass

    if input_main == '4':
        ip = input('IP Snnifing: ')
        def ipv(ip_addr):
            try:
                ipaddress.ip_address(ip_addr)
                return True
            except ValueError:
                return False

        print('┌───────────────────────────────────────────────────────────┐\u001B[36m')
        if (ipv(ip)):
            print(ip, 'is valid.')
        else:
            print(ip, 'is invalid.')

        url = "http://ip-api.com/json/{0}"
        response = requests.get(url.format(ip)).json()
        for key in response:
            print("{0: <15} - {1}".format(key, response[key]))

        print('\u001b[32;1m└───────────────────────────────────────────────────────────┘\u001B[36m')

        time.sleep(2)
        _main_()
    else:
        pass

    if input_main == '5':
        print('\u001b[32;1m┌───────────────────────────────────────────────────────────┐\u001B[36m')
        for ping in range(1,10):
            address = "127.0.0." + str(ping)
            res = subprocess.call(['ping', '-c', '3', address])
            if res == 0:
                print( "!!! IP", address, "is not stealth !!!")
            elif res == 2:
                print("no response from", address)
            else:
                print("IP", address, "is stealth")
        print('\u001b[32;1m└───────────────────────────────────────────────────────────┘\u001B[36m')
        time.sleep(2)
        _main_()
    else:
        pass

    if input_main == '6':
        hostname = socket.gethostname()
        target = socket.gethostbyname(hostname)

        print('\u001b[32;1m┌────────────────────────────────────────────────────┐\u001B[36m')
        print("Scanning target: " + target)
        print("Scanning started at: " + str(datetime.now()))
        print('\u001b[32;1m──────────────────────────────────────────────────────\u001B[36m')
        try:
            for port in range(1,65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)

                # returns an error indicator
                result = s.connect_ex((target,port))
                if result ==0:
                    print("Port {} is open to public".format(port))
                s.close()

            print('\u001b[32;1m└────────────────────────────────────────────────────┘\u001B[36m')

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
        _main_()
    else:
        pass

time.sleep(1)
_main_()
print('\u001b[0m')
