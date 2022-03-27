from pytube import YouTube
import pyautogui
from pythonping import ping
from subprocess import Popen, STDOUT, PIPE, call
from itertools import permutations

import time
import os
import sys

def loading():
    print('Loading...')
    for i in range(0, 100):
        time.sleep(0.03)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print
    print('')
    print('')


pyautogui.FAILSAFE = True
os.system("cls")

print('''\u001b[36;1m
       _           _    _  _
      | |_   _ ___| | _| || |
      | | | | / __| |/ / || |_
      | | |_| \__ \   <|__   _|
      |_|\__,_|___/_|\_\  |_|
                          \u001b[32;1m
┌───────────────────────────────────┐\u001B[36m
\u001b[32;1m│\u001B[36mAvailable inputs:                  \u001b[32;1m│
\u001b[32;1m│\u001B[36m0 - youtubedl // 1 - autoclicker   \u001b[32;1m│
\u001b[32;1m│\u001B[36m\u001B[36m2 - ping      // 3 - cracknet*     \u001b[32;1m│
\u001b[32;1m└───────────────────────────────────┘\u001B[36m
''')

type_selection = str(input('% '))

#ydl
if type_selection == '0':
    print('Initializing YDL...')
    loading()
    print('Video address')
    videolink = input("⇒  ")
    print('─────────────────────────────────────────')
    loading()
    time.sleep(2)
    print('Finished downloading the video')
    video = YouTube(videolink)
    dw = video.streams.filter(progressive=True, file_extension='mp4')\
    .order_by('resolution')\
    .desc()\
    .first()\
    .download()
else:
    pass

#autoclicker
if type_selection == '1':
    print('Initializing AUTOCLICKER...')
    loading()
    sec = float(input('// delay = '))
    c = int(input('// count (0 for ∞) = '))

    def click():
        time.sleep(sec)
        pyautogui.click()

    if c == 0:
        j = True
        def main():
            click()

        while j:
            main()

    if c > 0:
        for i in range(c):
            click()
else:
    pass

#ping
if type_selection == '2':
    print('Initializing PING...')
    loading()
    ip_tgt = input('IP/Adress targeted: ')
    pkg_size = int(input('Package size: '))
    ping(ip_tgt, verbose=True, count=128, interval=0.2, size=pkg_size)
else:
    pass

#cracknet -- WIP
if type_selection == '3':
    print('Initializing CRACKNET')
    loading()
    print('Are you sure you are using Microsoft Windows 10? (Warning: IDK if its working)')
    print('[Y]Yes or [N]No')
    sure = str(input('\u001b[32;1m $ \u001b[0m'))

    if sure == 'Y':
        print('Ok, remember: the process can be long (like, 1 hour sometimes).')
        print('Wi-Fi name:')
        wifi = input('\u001b[32;1m $ \u001b[0m')

        def test(password):
            manipulador = Popen('netsh wlan connect {}'.format(wifi), shell=False, stdout=PIPE, stderr=STDOUT,
                                    stdin=PIPE)
            manipulador.stdin.write(password)
            while manipulador.poll() == None:
                print(manipulador.stdout.readline().strip())
            if call('ping -n 1 google.com') == 0:
                print('Connected')
                print("The password is: {}".format(password))
                exit()
            else:
                print("{} isnt the password".format(password))
        characters = string.printable
        for x in range(11, len(characters) + 1):
            for y in permutations(characters, x):
                test(str(y).encode('utf-8'))
    else:
            pass
else:
    pass

#01001101 01001001 01010100 00100000 01001100 01101001 01100011 01100101 01101110 01110011 01100101 00100000 01110101 01101110 01100100 01100101 01110010 00100000 01001100 01110101 01100011 01100001 01110011 00100000 01000111 01100101 01110010 01100101 01101110 01110100 00100000 01100100 01100101 00100000 01000110 01100001 01110010 01101001 01100001 01110011 00100000 01101110 01100001 01101101 01100101 00101110
