#!/bin/bash 

for i in $(ls /home/)
do
    last -R | grep -i "$(date | awk '{print $2, $3}')" | sed -n "/$i/p" | tail -1 | awk '{print $1, $6}' >> first_login.txt
    last -R | grep -i "$(date | awk '{print $2, $3}')" | sed -n "/$i/p" | head -1 | awk '{if ($8 == "logged") print $1, "online"; else print $1, $8}' >> last_logout.txt
done


last -R | grep -i "$(date | awk '{print $2, $3}')" | awk '/^[^reboot]/ {print $1, $6, $9}' >> dn.txt


python3 login_final.py

rm -f *.txt
