
echo "1.install"
echo "2.keluar"
read -p "pilih:  " pilih

if [ $pilih = "1" ]
then
   sudo apt install python3
   sudo pip3 install tdqm
   sudo pip3 install colorama

elif [ $pilih = "2" ]
then
    exit
    fi
   
