#!/bin/bash
clear
echo "
██████████████████████████████████████    
█▄─▀█▄─▄█▀▀▀▀▀██▄─▄███▄─▄█─▄─▄─█▄─▄▄─█ 
██─█▄▀─██████████─██▀██─████─████─▄█▀█   
▀▄▄▄▀▀▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▀▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀
       █ ▄▀█  █▀▄ █ ~ ☪ By Manisso ☪ ~           
      ▐▌          ▐▌
      █▌▀▄  ▄▄  ▄▀▐█ 
     ▐██  ▀▀  ▀▀  ██▌
    ▄████▄  ▐▌  ▄████▄                                                  
           

                                                ";

echo "[✔] Checking directories...";
if [ -d "/usr/share/doc/nlite" ] ;
then
echo "[◉] A directory nlite was found! Do you want to replace it? [Y/n]:" ; 
read mama
if [ $mama == "y" ] ; 
then
 rm -R "/usr/share/doc/nlite"
else
 exit
fi
fi

 echo "[✔] Installing ...";
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
echo "[✔]Tool istalled with success![✔]";
echo "";
  echo "[✔]====================================================================[✔]";
  echo "[✔] ✔✔✔  All is done!! You can execute tool by typing nlite  !  ✔✔✔ [✔]"; 
  echo "[✔]====================================================================[✔]";
  echo "";
else
  echo "[✘] Installation faid![✘] ";
  exit
fi