#Greet's To
#IcoDz - Canejo              
#Tool For Hacking 
#Authors : Manisso

clear

sudo rm -rf /usr/share/doc/nlite/

clear

echo "[✔] Updating .... [✔]";
 echo "";
 git clone https://github.com/Manisso/Nlite.git /usr/share/doc/nlite;
 echo "#!/bin/bash 
 python /usr/share/doc/nlite/main.py" '${1+"$@"}' > nlite;
 chmod +x nlite;
 sudo cp nlite /usr/bin/;
 rm nlite;


if [ -d "/usr/share/doc/nlite" ] ;
then
echo "";
echo "[✔]Tool Updated with success![✔]";
echo "";
nlite
else
  echo "[✘] Update Failed ! ![✘] ";
  exit
fi
