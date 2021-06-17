import os
from time import sleep
import sys
import signal
import colorama
from colorama import Fore
colorama.init()

if not os.geteuid() == 0:
        sys.exit("""\033[1;91m\n[!] wificrack harus dijalankan sebagai root. ¯\_(ツ)_/¯\n\033[1;m""")


print (Fore.GREEN + "ketik help untuk bantuan")
def main():
    
    p = input("wificrack: ")
    if p == "help":
        print ("__________________________________________________________")
        print ("|                                                        |")
        print ("|                (airodump-ng                            |")
        print ("|                (aireplay-ng                            |")
        print ("|                (aircrack-ng                            |")
        print ("|                (monitor mode                           |")  
        print ("|                (keluar                                 |")
        print ("|         (!) gunakan use untuk masuk ke file            |")
        print ("|         exemple: use (nama script)                     |")
        print ("|________________________________________________________|")
        main()
    elif p == "use airodump":
        airodump()
    elif p == "use aireplay-ng":
        aireplay()
    elif p == "use aircrack-ng":
        aicrack()
    elif p == "use monitor mode":
        startmoni()
    elif p == "keluar":
        keluar()


def airodump():
    airo = input("wificracker/airodump-ng : ")
    if airo == "help":
        print ("__________________________________________________________")
        print ("|                                                        |")
        print ("|                (scanwifi                               |")
        print ("|                (captures                               |")
        print ("|                (kembali                                |")
        print ("|________________________________________________________|")
        airodump()
    elif airo == "use scanwifi":
        inter = input("masukan nama interfaces yang anda gunakan: ")
        os.system ("airodump-ng " + inter)
        airodump()
    elif airo == "use captures":
        int = input("masukan interfaces: ")
        ch = input("masukan channel: ")
        bs = input ("masukan bssid: ")
        cui = input ("masukan nana untuk file baru")
        print ("buka terminal baru dan jalankan script hackwifi aircrack-ng atau areplay-ng script akan jalan 15 detik")
        sleep (15)
        os.system("airodump-ng -w " +cui+ " -c " + ch + " --bssid " + bs + int)
        airodump()
    elif airo == "kembali""use kembali":
        main()
    else:
        print ("command salah")
        airodump()

def aireplay():
    attack = input("wificrack/aireplay-ng : ")
    if attack == "help":
        print ("__________________________________________________________")
        print ("|                                                        |")
        print ("|                (attack wifi                            |")
        print ("|                (attack client wifi                     |")
        print ("|                (kembali                                |")
        print ("|________________________________________________________|")
        aireplay()
    elif attack == "use attack wifi":
        bs = input("masukan interface: ")
        dea = input("masukan deauth: " )
        bsid = input("masukan bssid: ")
        os.system("aireplay-ng --deauth " + dea + " -a " + bsid + bs)
        aireplay()
    elif attack == "use attack client wifi":
        client = input("masukan client: ")
        deau = input("masukan deauth: ")
        bssid  = input("masukan bssid: ")
        bs = input("masukan interface: ")
        os.system("aireplay-ng --deauth " + deau + " -a " + bssid + " -c " + client + bs)
        aireplay()
    elif attack == "kembali":
        main()
    else:
        print ("command salah")
        aireplay()

def aicrack():
    p = input("apakah anda yakin menjalankan aircrack-ng y/n: ")
    if p == "y":
        wr = input("masukan wordlist: ")
        capp = input("masukan file format .cap: ")
        os.system("aircrack-ng " + capp + " -w " + wr)
    elif p == "n":
        main()
    else:
        print ("command salah mengulang script")
        aicrack()

def startmoni():
    monit = input("wificrack/monitor-mode:  ")
    if monit == "help":
        print ("__________________________________________________________")
        print ("|                                                        |")
        print ("|                (cek interfaces                         |")
        print ("|                (start/stop                             |")
        print ("|                (kembali                                |")
        print ("|________________________________________________________|")
        startmoni()
    elif monit == "use start/stop":
        inter = input("masukan interfaces:")
        sta = input("apakah anda ingin start/stop interfaces: ")
        os.system("airmon-ng"+ sta + inter)
        startmoni()
    elif monit == "use cek interfaces":
        os.system("airmon-ng")
        startmoni()
    elif monit == "kembali":
        main()
    else:
        print ("nomor salah kembali ke menu")
        startmoni()
    
def keluar():
    print('\n(!) selamat tinggal (^-^)/\n')
    sys.exit()

def signal_handler(signal, frame):
    print('\n(!) selamat tinggal (^-^)/\n')
    sys.exit()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()