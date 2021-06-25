import os
from time import sleep
import sys
import signal
import colorama
import random
import itertools
import threading
import time
import sys
from random import betavariate, uniform
from tqdm import tqdm
from colorama import Fore
colorama.init()

if not os.geteuid() == 0:
        sys.exit("""\033[1;91m\n[!] wificrack harus dijalankan sebagai root. ¯\_(ツ)_/¯\n\033[1;m""")


done = False
def loading():
        for c in itertools.cycle(['Wificrack-tools', 'wIficrack-tools', 'wiFicrack-tools','wifIcrack-tools','wifiCrack-tools','wificRack-tools','wificrAck-tools','wificraCk-tools','wificracK-tools','wificrack—tools','wificrack-Tools','wificrack-tOols','wificrack-toOls','wificrack-tooLs','wificrack-toolS']):
            if done:
                break
            sys.stdout.write('\r' + c)
            sys.stdout.flush()
            time.sleep(0.1)
t = threading.Thread(target=loading)
t.start()
time.sleep(20)
done = True

for _ in tqdm(range(100), unit="keystrokes", desc="loading..", ascii=False):
    sleep(uniform(0.005, 00.1))


os.system("clear")
beritau = ["hack itu tidak mudah","wificrack mengunakan aircrack-ng","alan github:https://github.com/alanlol12","wificrack2.0 terinspirasi dari metasploit dan xerosploit","ketik tentang untuk mengetahui script lebih lanjut"]

sapaan = [""" 
 $$\      $$\ $$\  $$$$$$\  $$\                                        $$\       
$$ | $\  $$ |\__|$$  __$$\ \__|                                       $$ |      
$$ |$$$\ $$ |$$\ $$ /  \__|$$\  $$$$$$$\  $$$$$$\  $$$$$$\   $$$$$$$\ $$ |  $$\ 
$$ $$ $$\$$ |$$ |$$$$\     $$ |$$  _____|$$  __$$\ \____$$\ $$  _____|$$ | $$  |
$$$$  _$$$$ |$$ |$$  _|    $$ |$$ /      $$ |  \__|$$$$$$$ |$$ /      $$$$$$  / 
$$$  / \$$$ |$$ |$$ |      $$ |$$ |      $$ |     $$  __$$ |$$ |      $$  _$$<  
$$  /   \$$ |$$ |$$ |      $$ |\$$$$$$$\ $$ |     \$$$$$$$ |\$$$$$$$\ $$ | \$$\ 
\__/     \__|\__|\__|      \__| \_______|\__|      \_______| \_______|\__|  \__| """, """ 
 ____      ____  _     ___  _ 
|_  _|    |_  _|(_)  .' ..](_)                              [  |  _   
  \ \  /\  / /  __  _| |_  __   .---.  _ .--.  ,--.   .---.  | | / ]  
   \ \/  \/ /  [  |'-| |-'[  | / /'`\][ `/'`\]`'_\ : / /'`\] | '' <   
    \  /\  /    | |  | |   | | | \__.  | |    // | |,| \__.  | |`\ \  
     \/  \/    [___][___] [___]'.___.'[___]   \'-;__/'.___.'[__|  \_] """, """ 

db   d8b   db d888888b d88888b d888888b  .o88b. d8888b.  .d8b.   .o88b. db   dD 
88   I8I   88   `88'   88'       `88'   d8P  Y8 88  `8D d8' `8b d8P  Y8 88 ,8P' 
88   I8I   88    88    88ooo      88    8P      88oobY' 88ooo88 8P      88,8P   
Y8   I8I   88    88    88~~~      88    8b      88`8b   88~~~88 8b      88`8b   
`8b d8'8b d8'   .88.   88        .88.   Y8b  d8 88 `88. 88   88 Y8b  d8 88 `88. 
 `8b8' `8d8'  Y888888P YP      Y888888P  `Y88P' 88   YD YP   YP  `Y88P' YP   YD 
                                                                                 """,""" 
                                                                                 
888       888 d8b  .d888 d8b                                   888      
888   o   888 Y8P d88P"  Y8P                                   888      
888  d8b  888     888                                          888      
888 d888b 888 888 888888 888  .d8888b 888d888 8888b.   .d8888b 888  888 
888d88888b888 888 888    888 d88P"    888P"      "88b d88P"    888 .88P 
88888P Y88888 888 888    888 888      888    .d888888 888      888888K  
8888P   Y8888 888 888    888 Y88b.    888    888  888 Y88b.    888 "88b 
888P     Y888 888 888    888  "Y8888P 888    "Y888888  "Y8888P 888  888 """, """ 

                                       _..._                            _..._                   
                                    .-'_..._''.                      .-'_..._''.                
              .--.          .--.  .' .'      '.\                   .' .'      '.\    .          
       _     _|__|     _.._ |__| / .'                             / .'             .'|          
 /\    \\   //.--.   .' .._|.--.. '             .-,.--.          . '             .'  |          
 `\\  //\\ // |  |   | '    |  || |             |  .-. |    __   | |            <    |          
   \`//  \'/  |  | __| |__  |  || |             | |  | | .:--.'. | |             |   | ____     
    \|   |/   |  ||__   __| |  |. '             | |  | |/ |   \ |. '             |   | \ .'     
     '        |  |   | |    |  | \ '.          .| |  '- `" __ | | \ '.          .|   |/  .      
              |__|   | |    |__|  '. `._____.-'/| |      .'.''| |  '. `._____.-'/|    /\  \     
                     | |            `-.______ / | |     / /   | |_   `-.______ / |   |  \  \    
                     | |                     `  |_|     \ \._,\ '/            `  '    \  \  \   
                     |_|                                 `--'  `"               '------'  '---' """]
print (Fore.GREEN + "by alan", random.choice(sapaan))
print (random.choice(beritau))



print ( "ketik help untuk bantuan")
def main():
    
    p = input(Fore.CYAN + "wificrack > "+Fore.WHITE)
    if p == "help":
        print (Fore.GREEN + "__________________________________________________________")
        print ("|                                                        |")
        print (Fore.CYAN+"|                [!]"+Fore.RED+"airodump-ng                          |")
        print (Fore.CYAN+"|                [!]"+Fore.GREEN+"aireplay-ng                          |")
        print (Fore.CYAN+"|                [!]"+Fore.WHITE+"aircrack-ng                          |")
        print (Fore.CYAN+"|                [!]"+Fore.YELLOW+"monitor mode                         |")  
        print (Fore.CYAN+"|                [!]"+Fore.MAGENTA+"keluar                               |")
        print (Fore.CYAN+"|                (!)"+Fore.LIGHTBLUE_EX+"gunakan use untuk masuk ke file      |")
        print (Fore.GREEN+"|               exemple:"+Fore.BLUE+"use (nama script)                |")
        print (Fore.GREEN+"|________________________________________________________|")
        main()
    elif p == "use airodump-ng":
        airodump()
    elif p == "use aireplay-ng":
        aireplay()
    elif p == "use aircrack-ng":
        aicrack()
    elif p == "use monitor mode":
        startmoni()
    elif p == "tentang":
        tentang()
    elif p == "keluar":
        keluar()
    else:
        print ("command salah")
        main()


def airodump():
    airo = input(Fore.CYAN + "wificracker/airodump-ng > "+Fore.WHITE)
    if airo == "help":
        print (Fore.GREEN + "__________________________________________________________")
        print ("|                                                        |")
        print (Fore.CYAN+"|                [!]"+Fore.RED+"scanwifi                             |")
        print (Fore.CYAN+"|                [!]"+Fore.YELLOW+"captures                             |")
        print (Fore.CYAN+"|                [!]"+Fore.MAGENTA+"kembali                              |")
        print (Fore.GREEN+"|________________________________________________________|")
        airodump()
    elif airo == "scanwifi":
        inter = input("masukan nama interfaces yang anda gunakan: ")
        os.system ("airodump-ng " + inter)
        airodump()
    elif airo == "captures":
        int = input("masukan interfaces: ")
        ch = input("masukan channel: ")
        bs = input ("masukan bssid: ")
        cui = input ("masukan nama untuk file baru: ")
        print ("buka terminal baru dan jalankan script hackwifi aircrack-ng atau areplay-ng script akan jalan 15 detik")
        sleep (15)
        os.system("airodump-ng -w " +cui+ " -c " + ch + " --bssid " + bs + " " + int)
        airodump()
    elif airo == "kembali":
        main()
    else:
        print ("command salah")
        airodump()

def aireplay():
    attack = input(Fore.CYAN + "wificrack/aireplay-ng > "+Fore.WHITE)
    if attack == "help":
        print (Fore.GREEN + "__________________________________________________________")
        print ("|                                                        |")
        print (Fore.CYAN+"|                [!]"+Fore.BLUE+"attack wifi                          |")
        print (Fore.CYAN+"|                [!]"+Fore.YELLOW+"attack client wifi                   |")
        print (Fore.CYAN+"|                [!]"+Fore.RED+"kembali                              |")
        print (Fore.GREEN+"|________________________________________________________|")
        aireplay()
    elif attack == "attack wifi":
        bs = input("masukan interface: ")
        dea = input("masukan deauth: " )
        bsid = input("masukan bssid: ")
        os.system("aireplay-ng --deauth " + dea + " -a " + bsid + " " + bs)
        aireplay()
    elif attack == "attack client wifi":
        client = input("masukan client: ")
        deau = input("masukan deauth: ")
        bssid  = input("masukan bssid: ")
        bs = input("masukan interface: ")
        os.system("aireplay-ng --deauth " + deau + " -a " + bssid + " -c " + client + " " + bs)
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
        main()
    elif p == "n":
        main()
    else:
        print ("command salah mengulang script")
        aicrack()

def startmoni():
    monit = input(Fore.CYAN + "wificrack/monitor-mode >  "+Fore.WHITE)
    if monit == "help":
        print (Fore.GREEN + "__________________________________________________________")
        print ("|                                                        |")
        print (Fore.CYAN+"|                [!]"+Fore.RED+"cek interfaces                       |")
        print (Fore.CYAN+"|                [!]"+Fore.YELLOW+"start/stop                           |")
        print (Fore.CYAN+"|                [!]"+Fore.BLUE+"kembali                              |")
        print (Fore.GREEN+"|________________________________________________________|")
        startmoni()
    elif monit == "start/stop":
        os.system("airmon-ng")
        inter = input("masukan interfaces:")
        sta = input("start/stop?: ")
        os.system("airmon-ng " + sta + " " + inter)
        startmoni()
    elif monit == "cek interfaces":
        os.system("airmon-ng")
        startmoni()
    elif monit == "kembali":
        main()
    else:
        print ("nomor salah kembali ke menu")
        startmoni()

def tentang():
    print (Fore.CYAN+"[!] "+Fore.RED+"pembuat: alan")
    print (Fore.CYAN+"[!] "+Fore.YELLOW+"github: https://github.com/alanlol12")
    print (Fore.CYAN+"[!] "+Fore.YELLOW+"wificrack2.0 di buat oleh alan wificrack2.0 adalah pengemabangan dari wificrack sebelumnya wificrack2.0 terispirasi dari metasploit dan xerosploit,wificrack juga mengunakan aircrack-ng untuk menjalankan script.")
    main()

def keluar():
    print(Fore.RED + '\n(!) selamat tinggal (^-^)/\n')
    sys.exit()

def signal_handler(signal, frame):
    print(Fore.RED + '\n(!) selamat tinggal (^-^)/\n')
    sys.exit()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()