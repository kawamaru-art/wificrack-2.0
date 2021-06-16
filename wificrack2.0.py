import os
from time import sleep
import sys

print ("ketik help untuk bantuan")
def main():
    p = input("wificrack: ")
    if p == "help":
        print ("__________________________________________________________")
        print ("|                                                        |")
        print ("|                (airodump-ng                            |")
        print ("|                (aireplay-ng                            |")
        print ("|                (aircrack-ng                            |")
        print ("|                (start monitor mode                     |")
        print ("|                (stop monitor mode                      |")  
        print ("|                (keluar                                 |")
        print ("|         (!) gunakan use untuk masuk ke file            |")
        print ("|         exemple: use (nama script)                     |")
        print ("|________________________________________________________|")
        main()
    elif p == "airodump":
        airodump()

def airodump():
    airo = input("wificracker/airodump-ng: ")
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
        main()

main()